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


# should be passed the output of parse_and_sort_gdscript
# will return a github markdown text
# does not create a file
def get_doc_text(arg_structured_gdscript_output: dict):
    # print("\nverifying")
    assert(verify_doc_text_input(arg_structured_gdscript_output) == True)
    # print("verified!")
    pass
    


# should be passed the output of parse_and_sort_gdscript
# will validate that nothing has changed/keys are as expected
def verify_doc_text_input(arg_output_from_parser: dict) -> bool:
    # verify the input is a dictionary with the exact keys required
    is_valid = True
    for expected_key in structured_input_format:
        if not expected_key in arg_output_from_parser.keys():
            print(f"verify_doc_text_input: key {key} exists in expected input but not passed get_doc_text input")
            is_valid = False
    for actual_key in arg_output_from_parser.keys():
        if not actual_key in structured_input_format:
            print(f"verify_doc_text_input: key {actual_key} exists in get_doc_text input but not expected input")
            is_valid = False
    return is_valid

