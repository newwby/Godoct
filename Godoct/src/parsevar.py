import re

## NOTE that class property and function definitions aren't being picked up because they're indented

def infer_type(arg_string):
    arg_string = str(arg_string)
    if "\"" in arg_string:
        return "string"
    elif arg_string == "true" or arg_string == "false":
        return "bool"
    elif "." in arg_string:
        return "float"
    elif "[" in arg_string:
        return "array"
    elif "{" in arg_string:
        return "dictionary"
    elif str(arg_string).isnumeric:
        return "int"
    elif arg_string[1:].isnumeric:
        return "int"
    else:
        return "unknown"

# should be passed an open file content
def find_var_data(arg_file_lines):
    
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
        cleaned_var_line = var_line.replace("\n", "")
        cleaned_var_line = cleaned_var_line.replace("\\", "")
        cleaned_var_line = re.sub(r'[ \t]+', ' ', cleaned_var_line)
        var_data = parse_var_line(cleaned_var_line)
        cleaned_doc_line = doc_line.replace("#", "")
        cleaned_doc_line = cleaned_doc_line.replace("\n", "")
        cleaned_doc_line = re.sub(r'[ \t]+', ' ', cleaned_doc_line.strip())
        var_data["documentation"] = cleaned_doc_line
        var_data_output.append(var_data)
        var_line = ""
        doc_line = ""
    
    def parse_var_line(arg_line):
        output = {
            "prefix": "",
            "name": "",
            "type": "",
            "default": "",
        }
        var_prefix = ""
        var_remainder = ""
        for possible_prefix in ["var", "const", "enum"]:
            if possible_prefix in arg_line:
                var_prefix = str(arg_line.split(possible_prefix)[0]+f" {possible_prefix}").strip()
                var_remainder = arg_line.split(possible_prefix)[1].strip()
        output["prefix"] = var_prefix

        var_name = ""
        var_default = ""
        var_type = ""
        # if inferred type from default arg
        if ":=" in var_remainder:
            var_remainder = var_remainder.split(":=")
            var_name = var_remainder[0].strip()
            var_default = var_remainder[1].strip()
            var_type = infer_type(var_default)
        else:
            # get specified type and default arg
            if ":" in var_remainder and "=" in var_remainder:
                var_remainder = var_remainder.split(":")
                var_name = var_remainder[0]
                var_remainder[1] = var_remainder[1].split("=")
                var_type = var_remainder[1][0]
                var_default = var_remainder[1][1]
            # get specified type and ignore default arg
            elif ":" in var_remainder and not "=" in var_remainder:
                var_remainder = var_remainder.split(":")
                var_name = var_remainder[0]
                var_type = var_remainder[1]
            # get default arg ignore specified type
            elif "=" in var_remainder and not ":" in var_remainder:
                var_remainder = var_remainder.split("=")
                var_name = var_remainder[0]
                var_default = var_remainder[1]
                # print(f"name {var_name} default is {var_default}")
            # ignore default and type
            else:
                var_name = var_remainder
            
            var_name = var_name.strip()
            var_default = var_default.strip()
            var_type = var_type.strip()

            # get default arg
            # if "=" in var_remainder:
            #     var_remainder = var_remainder.split("=")
            #     var_name = var_remainder[0].strip()
            #     var_type = var_remainder[1].strip()

        output["name"] = var_name
        output["default"] = var_default
        output["type"] = var_type


        return output

    # iterate through the file
    for line in arg_file_lines:
        
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
