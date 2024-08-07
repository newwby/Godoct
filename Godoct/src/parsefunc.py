import re

# should be passed an open file content
def find_function_data(arg_gdfile):
    # tracking multiline function declarations
    func_line = ""
    building_func_line = False
    # final output
    function_data_output = []

    documentation_line = ""
    for line in arg_gdfile.readlines():
        
        # build function declaration line
        if not building_func_line:
            if line.startswith("func") or line.startswith("static func"):
                func_line = ""
                func_line += line
                building_func_line = True
            else:
                # keep track of any documentation above functions
                if line.startswith("##"):
                    documentation_line += line
                else:
                    documentation_line = ""
        else:
            func_line += line
        
        # end building when hitting the :
        if building_func_line and line.strip().endswith(":"):
            building_func_line = False
            # clean the line and parse it into a dict
            cleaned_line = re.sub(r'[ \t]+', ' ', func_line)
            function_line_as_dict = parse_function_line(cleaned_line.replace("\n", ""))
            # store the documentation lines above the function
            clean_documentation = documentation_line.replace("#", "").replace("\n", " ").strip()
            clean_documentation = re.sub(r'[ \t]+', ' ', clean_documentation)
            # add docs to the dict
            function_line_as_dict["documentation"] = clean_documentation
            # output
            function_data_output.append(function_line_as_dict)
            # reset
            func_line = ""
            documentation_line = ""
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
