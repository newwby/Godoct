import os
import parsefunc
import parsevar
import generator_md

# TODO add more type hinting in func arguments and statically type func return values

# TODO create different mains for generating markdown versus generating rst
#   (move the validating logic to separate pyfile)
#   (move the parsing/sorting logic to separate pyfile)

# TODO write docs/walkthrough on how to write docs for GDscript files to pick up
#   specify about using ## documentation lines
#   specify how documentation lines must precede properties/functions
#   specify about class docstring and how to use empty lines
#   give examples
#   specify how the include file works

# TODO add docstrings for sphinx/rtd to pick up
#   write readme/landing page about Godoct for Github and another for RTD index

####################################

# TODO move to separate constants file

#TODO REMOVE LATER WHEN ADDING PROPER TESTING
# absolute path
TEST_FILE_PATH = "C:\\Users\\Daniel\\PycharmProjects\\Godoct\\src\\test_file.gd"

GODOCT_INCLUDE_FILE_NAME = "godoct_include.txt"
# move to consts
GODOCT_DOCS_DIRECTORY = "docs"

# class documentation always has to start with a line with this tag
DOC_START_TAG = "## <class_doc>"
# a paragraph break (two line breaks) can be added to documentation by adding a line that has no other characters except for this
DOC_EMPTY_LINE = "##"

####################################

# finds all .gd files within the same directory
def get_all_gdscript_paths():
    from os import walk

    dir_path = get_own_directory()
    try:
        assert(isinstance(dir_path, str)) == True
    except:
        print("invalid path")
        return ""

    # list to store full file path
    all_file_paths = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        for file_name in file_names:
            if isinstance(file_name, str):
                if file_name.endswith(".gd"):
                    all_file_paths.append(os.path.join(dir_path, file_name))
    return all_file_paths


# finds the include file within the same directory, then reads the lines within
# if cannot be found, creates an empty include file
def get_included_file_names():
    include_file_path = get_own_directory()+"\{0}".format(GODOCT_INCLUDE_FILE_NAME)
    include_file_text = []
    try:
        with open(include_file_path, "r") as f:
            names_list = [l for l in (line.strip() for line in f) if l]
        include_file_text = names_list
    except:
        print("no included files, writing blank include file and no docs will be generated")
        with open(include_file_path, 'w') as f:
            f.write('')
    return include_file_text


# make sure to pass include as first
def get_matched_gdscripts(arg_allowed_file_names, arg_file_paths):
    # debug prints
    # print(f"\ntest print list 1 = {arg_allowed_file_names}")
    # print(f"\ntest print list 2 = {arg_file_paths}")
    output = []
    for file_path in arg_file_paths:
        file_name = os.path.basename(file_path)
        if isinstance(file_name, str) and file_name in arg_allowed_file_names:
            output.append(file_path)
    # print(f"\nvalid output = {output}")
    return output


# returns path to this script's directory
def get_own_directory():
    import sys
    script_path = os.path.realpath(sys.argv[0])
    return os.path.dirname(script_path)


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
def parse_and_sort_gdscript(arg_gdscript_file_path):
    file_content = []
    try:
        gdfile = open(arg_gdscript_file_path)
        file_content = gdfile.readlines()
    except:
        print("file open error")
    
    if len(file_content) > 1:
        
        # file detail
        script_name = ""
        is_tool_script = False
        class_parent = ""
        class_name = ""
        class_documentation = ""

        # get basic script detail
        script_name = os.path.basename(arg_gdscript_file_path)
        
        collecting_documentation = False
        class_docstring = ""

        # collect script information by iterating through the file
        for line in file_content:
            if line.strip().startswith("@tool"):
                is_tool_script = True
            if line.strip().startswith("extends"):
                class_parent = line.split("extends")[1].strip()
            if line.strip().startswith("class_name"):
                class_name = line.split("class_name")[1].strip()
            
            if collecting_documentation:
                # collect all consecutive lines that are valid documentation lines
                if line.startswith("##"):
                    class_docstring += line.replace("\n", "").replace("##", "").strip()+" "
                    if line.strip() == DOC_EMPTY_LINE:
                        class_docstring += "\n\n"
                # if invalid line, store the documentation
                else:
                    collecting_documentation = False
                    class_documentation = class_docstring
                    class_docstring = ""
            # class documentation must start with a line with the start tag
            if line.startswith(DOC_START_TAG):
                collecting_documentation = True
        
        # collect and collate property and function information
        output_all_properties = parsevar.find_var_data(file_content)
        output_all_functions = parsefunc.find_function_data(file_content)

        # sort properties into constituent lists
        all_signals = []
        all_enums = []
        all_consts = []
        all_export_vars = []
        all_public_vars = []
        all_private_vars = []
        all_onready_vars = []

        # properties are organised by the prefix first (variables are further organised by name)
        for property_entry in output_all_properties:
            if isinstance(property_entry, dict):
                if "prefix" in property_entry:
                    assert(isinstance(property_entry["prefix"], str))
                    # sort by type to the correct list
                    if "signal" in property_entry["prefix"]:
                        all_signals.append(property_entry)
                    elif "enum" in property_entry["prefix"]:
                        all_enums.append(property_entry)
                    elif "const" in property_entry["prefix"]:
                        all_consts.append(property_entry)
                    
                    # extra categorising for variables
                    elif "var" in property_entry["prefix"]:
                        # get if export variant or onready
                        if property_entry["prefix"].startswith("@export"):
                            all_export_vars.append(property_entry)
                        elif property_entry["prefix"].startswith("@onready"):
                            all_onready_vars.append(property_entry)
                        # sort by public/private
                        else:
                            if "name" in property_entry:
                                assert(isinstance(property_entry["name"], str))
                                if property_entry["name"].startswith("_"):
                                    all_private_vars.append(property_entry)
                                else:
                                    all_public_vars.append(property_entry)

        # sort properties into constituent lists
        all_static_funcs = []
        all_public_funcs = []
        all_private_funcs = []

        # properties are organised by the prefix first (variables are further organised by name)
        for property_entry in output_all_functions:
            if isinstance(property_entry, dict):
                if "prefix" in property_entry:
                    assert(isinstance(property_entry["prefix"], str))
                    if property_entry["prefix"] == "static func":
                        all_static_funcs.append(property_entry)
                    # extra handling for if not static
                    elif property_entry["prefix"] == "func":
                        if "name" in property_entry:
                            assert(isinstance(property_entry["name"], str))
                            if property_entry["name"].startswith("_"):
                                all_private_funcs.append(property_entry)
                            else:
                                all_public_funcs.append(property_entry)

        output_structure = {
            "script_name": script_name,
            "is_tool": is_tool_script,
            "class_parent": class_parent,
            "class_name": class_name,
            "class_documentation": class_documentation,
            "signals": all_signals,
            "enums": all_enums,
            "constants": all_consts,
            "exports": all_export_vars,
            "onready": all_onready_vars,
            "public_var": all_public_vars,
            "private_var": all_private_vars,
            "static_funcs": all_static_funcs,
            "public_funcs": all_public_funcs,
            "private_funcs": all_private_funcs,
            # "_all_properties": output_all_properties,
            # "_all_functions": output_all_properties,
        }

        # TESTING ONLY/REMOVE FOR LIVE
        debug_print_output_structure = True
        if debug_print_output_structure:
            print(f"\nDEBUGGING OUTPUT FOR SCRIPT @ {arg_gdscript_file_path}")
            for key in output_structure:
                value = output_structure[key]
                if isinstance(value, list):
                    print(f"\noutputting {key}".upper())
                    for i in value:
                        print(i)
                else:
                    print(f"{key}: {value}")

            return output_structure

# is __main__
valid_paths = get_matched_gdscripts(get_included_file_names(), get_all_gdscript_paths())
# for path in get_matched_gdscripts(get_included_file_names(), get_all_gdscript_paths())
#   generate_markdown(parse_and_sort_gdscript(path))
parse_and_sort_gdscript(TEST_FILE_PATH)
generator_md.get_doc_text(parse_and_sort_gdscript(TEST_FILE_PATH))
