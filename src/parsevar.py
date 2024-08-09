import re
import utilparser

## NOTE that class property and function definitions aren't being picked up because they're indented

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
        var_data = {}
        if cleaned_var_line.startswith("signal"):
            var_data = parse_signal_line(cleaned_var_line)
        else:
            var_data = parse_var_line(cleaned_var_line)
        cleaned_doc_line = doc_line.replace("#", "")
        cleaned_doc_line = cleaned_doc_line.replace("\n", "")
        cleaned_doc_line = re.sub(r'[ \t]+', ' ', cleaned_doc_line.strip())
        var_data["documentation"] = cleaned_doc_line
        var_data_output.append(var_data)
        var_line = ""
        doc_line = ""
    
    def parse_signal_line(arg_line):
        # signal arguments can be typed
        # prefix is always signal
        output = {
            "prefix": "signal",
            "name": "",
            "arguments": "",
        }
        signal_name = arg_line.split("signal", 1)[1].strip()
        if "(" in signal_name:
            signal_name = signal_name.split("(")[0].strip()
        output["name"] = signal_name

        if "(" in arg_line:
            all_arguments = arg_line.split("(")[1].replace(")", "").strip()
            all_arguments = all_arguments.split(",")
            output_arguments = []
            for signal_argstr in all_arguments:
                signal_argument_data = {"name": "", "type": ""}
                signal_argument_as_tuple = utilparser.categorise_property(signal_argstr)
                signal_argument_data = {
                    "name": signal_argument_as_tuple[0],
                    "type": signal_argument_as_tuple[1],
                }
                output_arguments.append(signal_argument_data)

            output["arguments"] = output_arguments

        return output

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

        # enums get different handling
        if "enum" in var_prefix:
            var_remainder = var_remainder.split("{")
            var_name = var_remainder[0].strip()
            var_default = var_remainder[1].strip()
            var_default = var_default.strip().replace("}", "")
            var_type = "enum"

        # var and const parsing
        else:
            parsed_var_tuple = utilparser.categorise_property(var_remainder)   
            var_name = parsed_var_tuple[0]
            var_type = parsed_var_tuple[1]
            var_default = parsed_var_tuple[2]

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
        or strline.startswith("var") or (strline.startswith("@") and "var" in strline)\
        or strline.startswith("signal"):
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

