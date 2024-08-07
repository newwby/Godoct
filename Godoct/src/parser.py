import os
import re

GODOCT_DOCS_DIRECTORY = "docs"
TEST_FILE_PATH = "C:\\Users\\Daniel\\PycharmProjects\\Godoct\\Godoct\\src\\test_file.gd"


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

    try:
        gdfile = open(arg_gdscript_file_path)
    except:
        print("file open error")
        return

    func_line = ""
    building_func_line = False
    functions = []
    for line in gdfile.readlines():
        if not building_func_line:
            if line.startswith("func"):
                func_line = ""
                func_line += line
                building_func_line = True
        else:
            func_line += line
        if building_func_line and line.strip().endswith(":"):
            building_func_line = False
            # re.sub('\s{2,}', ' ', func_line)
            cleaned_line = re.sub(r'[ \t]+', ' ', func_line)
            functions.append(cleaned_line.replace("\n", ""))
            func_line = ""
    for i in functions:
        print(i)
    print("I AM PARSER")
    print("!")


if __name__ == "__main__":
    parse_gdscript_file(TEST_FILE_PATH)


