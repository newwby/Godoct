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

    def get_gdscript_file_text():
        # nonlocal arg_gdscript_file_path
        try:
            f = open(arg_gdscript_file_path)
            return f.read()
        except:
            return ""
    
    # load the file, this will be used repeatedly for fetching various information
    file_text = str(get_gdscript_file_text())
    assert(file_text != "")

    # get the script name
    file_path_script_name = os.path.basename(arg_gdscript_file_path)
    assert(str(file_path_script_name).endswith(".gd"))
    output_structure["script_name"] = file_path_script_name
    
    # identify function detail
    def find_function_lines():
        # find starting points
        func_match_pairs = []
        for match in re.finditer("\nfunc ", file_text):
            func_match_pairs.append((match.start(), match.end()))
        for match in re.finditer("\nstatic func ", file_text):
            func_match_pairs.append((match.start(), match.end()))
        
        # get the actual text
        function_lines = []
        for pair in func_match_pairs:
            end_of_func_index = pair[1]
            while file_text[end_of_func_index] != ")":
                end_of_func_index += 1
            while file_text[end_of_func_index] != ":":
                end_of_func_index += 1
            
            # add back the semicolon so it is a valid entry for parse_functions
            function_entry = file_text[pair[0]: end_of_func_index].replace("\n", "")+":"
            re.sub("\s\s+", " ", function_entry)
            function_lines.append(function_entry)
        print(function_lines)
        return function_lines
    
    def parse_functions(arg_functions):
        # Define the regex pattern
        pattern = re.compile(r'''
            ^\s*                      # Start of line, allowing for leading spaces
            (?P<prefix>static\s+)?    # Optional 'static' prefix
            func                      # The keyword 'func'
            \s+                       # One or more spaces
            (?P<name>\w+)             # Function name (one or more word characters)
            \s*                       # Optional spaces
            \(                        # Opening parenthesis for arguments
            (?P<arguments>[^)]*)      # Capture arguments (everything up to closing parenthesis)
            \)                        # Closing parenthesis
            \s*                       # Optional spaces
            (?P<return_type>->\s*\w+)? # Optional return type (starts with '->' followed by spaces and a type)
            \s*                       # Optional spaces
            :                         # End of the function line with a colon
            $                         # End of line
        ''', re.VERBOSE)

        # Parse and print the results
        for func in arg_functions:
            print(func)
            match = pattern.match(func)
            if match:
                print(f"Full match: {match.group(0)}")
                print(f"Prefix: {match.group('prefix')}")
                print(f"Name: {match.group('name')}")
                print(f"Arguments: {match.group('arguments')}")
                print(f"Return Type: {match.group('return_type')}")
                print()

    parse_functions(find_function_lines())



if __name__ == "__main__":
    parse_gdscript_file(TEST_FILE_PATH)


