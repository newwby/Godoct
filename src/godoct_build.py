import os

GODOCT_INCLUDE_FILE_NAME = "godoct_include.txt"

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
    print(f"\ntest print list 1 = {arg_allowed_file_names}")
    print(f"\ntest print list 2 = {arg_file_paths}")
    output = []
    for file_path in arg_file_paths:
        file_name = os.path.basename(file_path)
        if isinstance(file_name, str) and file_name in arg_allowed_file_names:
            output.append(file_path)
    print(f"\nvalid output = {output}")
    return output


# returns path to this script's directory
def get_own_directory():
    import sys
    script_path = os.path.realpath(sys.argv[0])
    return os.path.dirname(script_path)

import re

def parse_gdscript(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    functions = []
    current_comments = []
    
    func_pattern = re.compile(r'func\s+(\w+)\((.*?)\)(?:\s*->\s*(\w+))?:')
    comment_pattern = re.compile(r'#\s*(.*)')
    
    for line in lines:
        comment_match = comment_pattern.match(line)
        if comment_match:
            current_comments.append(comment_match.group(1))
            continue
        
        func_match = func_pattern.match(line)
        if func_match:
            func_name = func_match.group(1)
            args_str = func_match.group(2)
            return_type = func_match.group(3) if func_match.group(3) else 'void'
            
            args = []
            if args_str:
                args = [arg.strip() for arg in args_str.split(',')]
            
            functions.append({
                'name': func_name,
                'args': args,
                'return_type': return_type,
                'comments': current_comments
            })
            current_comments = []
    
    return functions

def generate_markdown(functions):
    markdown_lines = ['# GDScript Documentation\n']
    
    for func in functions:
        if func['comments']:
            markdown_lines.append('\n'.join([f'**{comment}**' for comment in func['comments']]))
        
        markdown_lines.append(f'### `{func["name"]}`')
        markdown_lines.append('```gdscript')
        args_str = ', '.join(func['args'])
        markdown_lines.append(f'func {func["name"]}({args_str}) -> {func["return_type"]}:')
        markdown_lines.append('```')
        markdown_lines.append('')
    
    return '\n'.join(markdown_lines)

def save_markdown(content, output_path):
    with open(output_path, 'w') as file:
        file.write(content)

# def main(gdscript_path, output_path):
#     functions = parse_gdscript(gdscript_path)
#     markdown_content = generate_markdown(functions)
#     save_markdown(markdown_content, output_path)
#     print(f"Markdown documentation generated: {output_path}")

# if __name__ == "__main__":
#     gdscript_path = 'path/to/your/script.gd'
#     output_path = 'path/to/output/documentation.md'
#     main(gdscript_path, output_path)


get_matched_gdscripts(get_included_file_names(), get_all_gdscript_paths())
