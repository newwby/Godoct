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
    doctext = ""
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
    output_body = ""
    for propdata in arg_parser_property_subsection:
        # validate entry
        assert(isinstance(propdata, dict))
        required_keys = ["prefix", "name", "type", "default", "documentation"]
        for key in required_keys:
            assert key in propdata.keys()
        prefix = propdata["prefix"]
        name = propdata["name"]
        type = propdata["type"]
        default = propdata["default"]
        documentation = propdata["documentation"]
        # print(prefix, name, type, default, documentation)
        output_body += f"{prefix} {name}: {type} = {default}\n-- {documentation}\n"
    
    return f"# {arg_subsection_name.upper()}\n{output_body}\n\n"

