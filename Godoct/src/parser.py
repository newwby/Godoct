import os
import re

GODOCT_DOCS_DIRECTORY = "docs"
TEST_FILE_PATH = "C:\\Users\\Daniel\\PycharmProjects\\Godoct\\Godoct\\src\\test_file.gd"


# should be passed a path to a gdscript file
# returns a dict of the contents structured as follows
"""{
    "script_name": a string representing the script file name,
    "class_parent": a string representing the extends attribute,
    "class_name": a string representing the class_name attribute,
    "class_documentation": a string representing documentation comments at the top of the script,
    "signals": a list of nested dictionaries where each dictionary details a signal in the script,
    "properties": a list of nested dictionaries where each dictionary details a property (var/const/enum) in the script,
    "functions": a list of nested dictionaries where each dictionary details a function in the script,
}"""
# with the exception of the 'script_name' property, the values to these keys can be empty (nil strings or empty lists)
def parse_gdscript_file(arg_gdscript_file_path):
    output_structure = {
        "script_name": "",
        "class_parent": "",
        "class_name": "",
        "class_documentation": "",
        "signals": [],
        "properties": [],
        "functions": [],
    }
    try:
        gdfile = open(arg_gdscript_file_path)
    except:
        print("file open error")
        return

    def find_function_data():
        # tracking multiline function declarations
        func_line = ""
        building_func_line = False
        # final output
        function_data_output = []

        for line in gdfile.readlines():
            if not building_func_line:
                if line.startswith("func") or line.startswith("static func"):
                    func_line = ""
                    func_line += line
                    building_func_line = True
            else:
                func_line += line
            if building_func_line and line.strip().endswith(":"):
                building_func_line = False
                # re.sub('\s{2,}', ' ', func_line)
                cleaned_line = re.sub(r'[ \t]+', ' ', func_line)
                function_line_as_dict = parse_function_line(cleaned_line.replace("\n", ""))
                function_data_output.append(function_line_as_dict)
                func_line = ""
        return function_data_output

    # pass find_functions as argument (an array of strings representing each function line)
    def parse_function_line(arg_function_line):
        # submethod to turn a string of function arguments into a dictionary
        # becomes an entry in the list under parsed_entry["arguments"]
        def parse_function_arguments(arg_function_arguments_string):
            if len(str(arg_function_arguments_string)) == 0:
                return {}
            else:
                args_separated = str(arg_function_arguments_string).strip().split(",")
                args_parsed = []
                for arg in args_separated:
                    categorised_args = {
                    "name": "",
                    "type": "",
                    "default": "",
                    }
                    arg_split = arg
                    arg_name = arg
                    if ":" in arg:
                        arg_type = str(arg.split(":")[1]).strip()
                    if "=" in arg_type:
                        arg_type = arg_type.split("=")[0].strip()
                    categorised_args["type"] = arg_type
                    if "=" in arg:
                        categorised_args["default"] = str(arg.split("=")[1].strip())
                    if "=" in arg_name:
                        arg_name = arg_name.split("=")[0].strip()
                    if ":" in arg_name:
                        arg_name = arg_name.split(":")[0].strip()
                    categorised_args["name"] = arg_name.strip()
                    args_parsed.append(categorised_args)
                        
                
                return args_parsed
        
        parsed_entry = {
            "prefix": False,
            "name": "NAME_NOT_FOUND",
            "arguments": [],
            "return": "unspecified"
        }
        # get if static or non-static function
        split_line = arg_function_line
        if "static func " in arg_function_line:
            parsed_entry["prefix"] = "static func"
            split_line = split_line.split("static func ")[1]
        elif "func " in arg_function_line:
            parsed_entry["prefix"] = "func"
            split_line = split_line.split("func ")[1]
        else:
            print("ERROR ", arg_function_line)
        
        # get function name
        parsed_entry["name"] = split_line.split("(")[0]
        parsed_entry["arguments"] = parse_function_arguments(split_line.split("(")[1].split(")")[0])
        
        # if a return type is specified in the function line, isolate it
        if "->" in split_line:
            parsed_entry["return"] = split_line.split("->")[1].strip().replace(":", "")
        
        return parsed_entry
    
    # pass find_functions as argument (an array of strings representing each function line)
    def parse_function_documentation(arg_function_lines, arg_include_private_functions = False):
        documentation_line = ""
        for line in gdfile.readlines():
            if line.startswith("##"):
                documentation_line += line
            else:
                documentation_line = ""
    
    function_output = find_function_data() #parse_functions(find_functions())
    # for i in function_output:
    #   # add function documentation by using name
    for i in function_output:
        print(i)


if __name__ == "__main__":
    parse_gdscript_file(TEST_FILE_PATH)


