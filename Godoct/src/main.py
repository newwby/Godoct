import os
import re
import parsefunc
import parsevar

GODOCT_DOCS_DIRECTORY = "docs"
GODOCT_INCLUDE_FILE_NAME = "godoct_include.txt"
#TODO REMOVE LATER
TEST_FILE_PATH = "C:\\Users\\Daniel\\PycharmProjects\\Godoct\\Godoct\\src\\test_file.gd"


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
    file_content = []
    try:
        gdfile = open(arg_gdscript_file_path)
        file_content = gdfile.readlines()
    except:
        print("file open error")
    
    if len(file_content) > 1:
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

        # TESTING ONLY/REMOVE FOR LIVE
        print("\nSIGNAL PROPERTIES")
        for i in all_signals:
            print(i)
        print("\nENUM PROPERTIES")
        for i in all_enums:
            print(i)
        print("\nCONST PROPERTIES")
        for i in all_consts:
            print(i)
        print("\nEXPORT VAR PROPERTIES")
        for i in all_export_vars:
            print(i)
        print("\nONREADY VAR PROPERTIES")
        for i in all_onready_vars:
            print(i)
        print("\nPUBLIC VAR PROPERTIES")
        for i in all_public_vars:
            print(i)
        print("\nPRIVATE VAR PROPERTIES")
        for i in all_private_vars:
            print(i)
        print("\nMETHODS")
        for i in output_all_functions:
            print(i)


valid_paths = get_matched_gdscripts(get_included_file_names(), get_all_gdscript_paths())
parse_gdscript_file(TEST_FILE_PATH)
