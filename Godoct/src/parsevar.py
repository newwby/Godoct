import re

## NOTE that class property and function definitions aren't being picked up because they're indented

# should be passed an open file content
def find_var_data(arg_gdfile):
    
    # final output for find_var_data
    var_data_output = []
    # tracking multiline property declarations
    var_line = ""
    doc_line = ""
    building_var_line = False

    # when hitting end of a variable declaration
    def output_var_data():
        nonlocal var_line
        nonlocal doc_line
        nonlocal building_var_line
        building_var_line = False
        cleaned_var_line = re.sub(r'[ \t]+', ' ', var_line)
        cleaned_var_line = cleaned_var_line.replace("\n", "")
        cleaned_doc_line = re.sub(r'[ \t]+', ' ', doc_line)
        cleaned_doc_line = cleaned_doc_line.replace("\n", "")
        var_data_output.append({
            "data": cleaned_var_line,
            "doc": cleaned_doc_line
            })
        var_line = ""
        doc_line = ""

    # iterate through the file
    for line in arg_gdfile.readlines():
        
        strline = str(line)

        line_is_documentation = strline.startswith("##")
        line_is_commented_out = strline.startswith("#")
        line_is_blank = len(strline.strip()) == 0

        # check if start of a property line
        # const, enum, var (with any @ prefix including @onready & @export variances) are valid
        if strline.startswith("const") or strline.startswith("enum")\
        or strline.startswith("var") or (strline.startswith("@") and "var" in strline):
            if building_var_line:
                output_var_data()
            building_var_line = True

        # stop building property and documentation strings on invalid line
        if (line_is_blank or line_is_commented_out):
            if var_line != "":
                output_var_data()
            if doc_line != "" and not line_is_documentation:
                doc_line = ""
        
        if building_var_line:
            var_line += line
        
        if line_is_documentation:
            doc_line += line
    
    # end
    return var_data_output


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
