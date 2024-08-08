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
def create_doc(arg_path, arg_doc_text):

    return


# should be passed the structured output of parse_and_sort_gdscript
# will return a github markdown text
# does not create a file
def get_doc_text(arg_parser_output: dict):
    if arg_parser_output is None:
        print("invalid argument for get_doc_text")
        return
    # print("\nverifying")
    assert(verify_doc_text_input(arg_parser_output) == True)
    # print("verified!")
    pass
    print("start header")
    print(_doc_text_header(arg_parser_output))
    print("end header")
    print("\n\n")
    print("start property read")
    print(_doc_text_properties(arg_parser_output))
    print("end property read")
    


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
    # (_generate_property_subsection(arg_parser_output["signals"])) # signals needs special handling it has different keys
    doctext += (_generate_property_subsection(arg_parser_output["enums"], "enums"))
    doctext += (_generate_property_subsection(arg_parser_output["constants"], "constants"))
    doctext += (_generate_property_subsection(arg_parser_output["exports"], "export var"))
    doctext += (_generate_property_subsection(arg_parser_output["onready"], "onready var"))
    doctext += (_generate_property_subsection(arg_parser_output["public_var"], "public var"))
    doctext += (_generate_property_subsection(arg_parser_output["private_var"], "private var"))
    
    return doctext


# from a property nested list (output from parse_and_sort gdscript) generates docs for properties within
def _generate_property_subsection(arg_parser_property_subsection: list, arg_subsection_name: str):
    # print("reading ", arg_parser_property_subsection)
    table_header = "| Property Name | Property Type | Propery Default Value |\n| --- | :---: | ---: |\n"
    full_table_output = ""
    full_entry_output = ""

    if len(arg_parser_property_subsection) == 0:
        return ""

    for propdata in arg_parser_property_subsection:
        # validate entry
        assert(isinstance(propdata, dict))
        required_keys = ["prefix", "name", "type", "default", "documentation"]
        for key in required_keys:
            assert key in propdata.keys()
        
        # assign entry values
        # prefix = propdata["prefix"]
        property_name = propdata["name"]
        property_type = propdata["type"]
        property_default = propdata["default"]
        property_docstring = propdata["documentation"]
        
        # build table
        table_line = f"| **{property_name}** | *{property_type}* | {property_default} |\n"
        full_table_output += table_line

        # build detailed entry
        print(f"0 1 2 3 {property_name} {property_type}")
        full_entry_output += f"### {property_name}"
        if len(property_type) > 0:
            full_entry_output += f"\n- **type:** {str(property_type).lower()}\n"
        if len(property_default) > 0:
            full_entry_output += f"\n- *[default value = {str(property_default).lower()}]*\n"
        if len(property_docstring) > 0:
            full_entry_output += f"\n{property_docstring}\n"
        
    #     detailed_entry_body = "### {property_name}\n{property_docstring}\n\"
    #     detailed_entry_body += "\n"

    #     full_entry_output += detailed_entry_body
        
    output_body = table_header+full_table_output+"\n"+full_entry_output
    subsection_name = arg_subsection_name.upper()
    if subsection_name.endswith("S") == False:
        subsection_name += "S"

    return f"\n---\n## {subsection_name}\n{output_body}\n\n"

