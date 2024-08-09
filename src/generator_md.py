
PROPERTY_SUBSECTION_KEYS = ["enums", "constants", "exports", "onready", "public_var", "private_var"]
CREDIT_LINK = "\n---\n*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*"

# expected keys for dict passed to get_doc_text
structured_input_format = [
        "script_name",
        "is_tool",
        "class_parent",
        "class_name",
        "class_documentation",
        "signals",
        "enums",
        "constants",
        "exports",
        "onready",
        "public_var",
        "private_var",
        "static_funcs",
        "public_funcs",
        "private_funcs"
    ]

# should be passed the file path to create the doc file and the output of get_doc_text
# overwrites the doc
def create_doc(arg_path, arg_doc_text):
    f = open(arg_path, "w")
    f.write(arg_doc_text)
    f.close()


# should be passed the structured output of parse_and_sort_gdscript
# will return a github markdown text
# does not create a file
def get_doc_text(arg_parser_output: dict):
    if arg_parser_output is None:
        print("invalid argument for get_doc_text")
        return
    assert(verify_doc_text_input(arg_parser_output) == True)
    text_header = _doc_text_header(arg_parser_output)
    sep = "\n\n"
    properties = _doc_text_properties(arg_parser_output)
    
    doc_text_output = f"{text_header}{sep}{properties}{CREDIT_LINK}"
    return doc_text_output
    


# should be passed the structured output of parse_and_sort_gdscript
# will validate that nothing has changed/keys are as expected
def verify_doc_text_input(arg_parser_output: dict) -> bool:
    # verify the input is a dictionary with the exact keys required
    is_valid = True
    for expected_key in structured_input_format:
        if not expected_key in arg_parser_output.keys():
            print(f"verify_doc_text_input: key {key} exists in expected input but not passed get_doc_text input")
            is_valid = False
    for actual_key in arg_parser_output.keys():
        if not actual_key in structured_input_format:
            print(f"verify_doc_text_input: key {actual_key} exists in get_doc_text input but not expected input")
            is_valid = False
    return is_valid


######################################################################


# should be passed validated (see verify_doc_text_input) output from parse_and_sort_gdscript
# generates the documentation header
def _doc_text_header(arg_parser_output: dict):
    # doc name is the class name, if specified, otherwise the basename for the script path minus the extnesion
    doc_name = ""
    if arg_parser_output["class_name"] != "":
        doc_name = arg_parser_output["class_name"]
    else:
        doc_name = arg_parser_output["script_name"].replace(".gd", "")
    
    # if it is a tool script, prefix with '@tool'
    if arg_parser_output["is_tool"] == True:
        doc_name = f"@tool {doc_name}"
    
    parent_class_name = arg_parser_output["class_parent"]
    documentation = arg_parser_output["class_documentation"]

    output_string = f"# {doc_name.upper()}\
    \n**Extends** {parent_class_name}\n\
        \n{documentation}\n"
    
    return output_string


# should be passed validated (see verify_doc_text_input) output from parse_and_sort_gdscript
# generates all the property bodies
def _doc_text_properties(arg_parser_output: dict):
    doctext = "# Properties\n\n"
    
    variable_table_text = "| | Property Name | Property Type | Property Default Value |\n| --- | :--- | :---: | ---: |\n"
    variable_entry_text = ""

    for subsect_key in PROPERTY_SUBSECTION_KEYS:
        variable_table_text += _generate_property_table_row(arg_parser_output[subsect_key])
        variable_entry_text += _generate_property_subsection(arg_parser_output[subsect_key], subsect_key)

    doctext = f"---\n# Properties\n{variable_table_text}\n{variable_entry_text}"

    # (_generate_property_subsection(arg_parser_output["signals"])) # signals needs special handling it has different keys
    doctext += (_generate_property_subsection(arg_parser_output["enums"], "enums"))
    doctext += (_generate_property_subsection(arg_parser_output["constants"], "constants"))
    doctext += (_generate_property_subsection(arg_parser_output["exports"], "export var"))
    doctext += (_generate_property_subsection(arg_parser_output["onready"], "onready var"))
    doctext += (_generate_property_subsection(arg_parser_output["public_var"], "public var"))
    doctext += (_generate_property_subsection(arg_parser_output["private_var"], "private var"))
    
    return doctext


# signals have different input and need argument restructuring, so 
def _generate_signal_subsection(arg_parser_property_subsection: list) -> str:
    pass


# checks whether a property subsection within the structured output of parse_and_sort (see 'PROPERTY_SUBSECTION_KEYS')
# is a valid type (dict) and has all valid keys for a subsection
def _validate_property_subsection(arg_property_subsect: list, arg_is_signal: bool = False) -> bool:
    if len(arg_property_subsect) < 1:
        # no error, sometimes subsections are empty
        # print("_validate_property_subsection length error")
        return False
    else:
        for propdata in arg_property_subsect:
            if isinstance(propdata, dict) == False:
                print("_validate_property_subsection type error")
                return False
            required_keys = []
            if arg_is_signal:
                required_keys = ["prefix", "name", "type", "arguments", "documentation"]
            else:
                required_keys = ["prefix", "name", "type", "default", "documentation"]
            for key in required_keys:
                if not key in propdata.keys():
                    print("_validate_property_subsection key error")
                    return False
    # else
    return True


# from a property nested list (output from parse_and_sort gdscript) generates docs for properties within
def _generate_property_subsection(arg_parser_property_subsection: list, arg_subsection_name: str) -> str:
    if (_validate_property_subsection(arg_parser_property_subsection) != True):
        return ""
    full_entry_output = ""

    for propdata in arg_parser_property_subsection:
        # assign entry values
        property_prefix = propdata["prefix"]
        property_name = propdata["name"]
        property_type = propdata["type"]
        property_default = propdata["default"]
        property_docstring = propdata["documentation"]

        # build detailed entry
        full_entry_output += f"### {property_prefix} {property_name}"
        if len(property_type) > 0:
            full_entry_output += f"\n- **type:** {str(property_type).lower()}\n"
        if len(property_default) > 0:
            full_entry_output += f"\n- *[default value = {str(property_default).lower()}]*\n"
        if len(property_docstring) > 0:
            full_entry_output += f"\n{property_docstring}\n"
        
    subsection_name = arg_subsection_name.upper()
    if subsection_name.endswith("S") == False:
        subsection_name += "S"

    return f"\n---\n## {subsection_name}\n{full_entry_output}\n\n"


def _generate_property_table_row(arg_parser_property_subsection: list) -> str:
    if (_validate_property_subsection(arg_parser_property_subsection) != True):
        return ""
    full_table_output = ""

    for propdata in arg_parser_property_subsection:
        # assign entry values
        property_prefix = propdata["prefix"]
        property_name = propdata["name"]
        property_name_link = f"{property_prefix}-{property_name}".replace(" ", "-").replace("@", "").lower()
        property_name = f"[{property_name}](#{property_name_link})"
        property_type = propdata["type"]
        property_default = propdata["default"]
        property_docstring = propdata["documentation"]
        
        # build table
        table_line = f"| {property_prefix} | **{property_name}** | *{property_type}* | {property_default} |\n"
        full_table_output += table_line
    
    return full_table_output
