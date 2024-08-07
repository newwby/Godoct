import os

GODOCT_DOCS_DIRECTORY = "docs"
TEST_FILE_PATH = "C:\\Users\\Daniel\\PycharmProjects\\Godoct\\Godoct\\src\\test_file.gd"

def infer_type_from_value(value):
    # Remove extra spaces and convert to lowercase for type checking
    value = value.strip().lower()
    
    # Attempt to infer the type based on the value
    if value.isdigit():
        return 'int'
    try:
        float(value)
        if '.' in value:
            return 'float'
        return 'int'
    except ValueError:
        pass
    if value in {'true', 'false'}:
        return 'bool'
    if value.startswith('"') and value.endswith('"'):
        return 'String'
    if value.startswith('[') and value.endswith(']'):
        return 'Array'
    if value.startswith('{') and value.endswith('}'):
        return 'Dictionary'
    if value.startswith('Resource(') and value.endswith(')'):
        return 'Resource'
    if value.startswith('Object(') and value.endswith(')'):
        return 'Object'
    return 'unknown'

def parse_gdscript_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    functions = []
    members = []
    signals = []
    class_documentation = []
    current_function = None
    current_signal = None
    member_documentation = []
    signal_documentation = []
    class_name = ''
    script_name = os.path.splitext(os.path.basename(file_path))[0]
    current_member = None
    inside_function = False
    inside_class = False
    first_function_found = False
    first_member_found = False
    parent_class = ''
    class_documentation_started = False
    documentation = []

    def process_current_function():
        nonlocal current_function
        if current_function:
            if current_function["function_name"] not in [f["function_name"] for f in functions]:
                current_function["documentation"] = " ".join(documentation).strip()
                functions.append(current_function)
            documentation.clear()
            current_function = None

    def process_member():
        nonlocal current_member
        if current_member:
            if current_member["name"] not in [m["member_name"] for m in members]:
                members.append({
                    "member_name": current_member["name"],
                    "member_type": current_member["type"],
                    "member_prefix": current_member["member_prefix"],
                    "member_value": current_member["value"],
                    "documentation": " ".join(member_documentation).strip()
                })
        member_documentation.clear()

    def process_current_signal():
        nonlocal current_signal
        if current_signal:
            if current_signal["signal_name"] not in [s["signal_name"] for s in signals]:
                current_signal["signal_documentation"] = " ".join(signal_documentation).strip()
                signals.append(current_signal)
            signal_documentation.clear()
            current_signal = None

    def process_class_documentation(line):
        nonlocal class_documentation_started
        if not class_documentation_started and not first_function_found and not first_member_found:
            class_documentation.append(line)

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if stripped_line.count('#') > 2:
            continue

        if stripped_line.startswith('##'):
            if not class_name and not inside_function and not inside_class:
                process_class_documentation(stripped_line[2:].strip())
            elif inside_class and not inside_function and not member_documentation and not current_signal:
                process_class_documentation(stripped_line[2:].strip())
            else:
                if inside_function:
                    documentation.append(stripped_line[2:].strip())
                elif current_member:
                    member_documentation.append(stripped_line[2:].strip())
                elif current_signal:
                    signal_documentation.append(stripped_line[2:].strip())

        elif stripped_line.startswith('func '):
            if not first_function_found:
                first_function_found = True
            if not class_name:
                class_documentation_started = True
            process_current_function()
            if stripped_line[5] == '_':
                continue
            
            func_def = stripped_line[5:]
            func_name_end = func_def.find('(')
            func_name = func_def[:func_name_end].strip()
            
            args_start = func_name_end + 1
            args_end = func_def.find(')')
            args_part = func_def[args_start:args_end].strip()
            
            return_value = ''
            if '->' in func_def:
                return_value = func_def.split('->')[1].split(':')[0].strip()
            
            args_list = args_part.split(',')
            function_arguments = []
            for arg in args_list:
                arg = arg.strip()
                if arg:
                    arg_name, arg_type, default_value = '', '', ''
                    if ':' in arg and '=' in arg:
                        arg_name, rest = arg.split(':', 1)
                        arg_type, default_value = rest.split('=', 1)
                    elif ':' in arg:
                        arg_name, arg_type = arg.split(':', 1)
                    elif '=' in arg:
                        arg_name, default_value = arg.split('=', 1)
                    else:
                        arg_name = arg
                    function_arguments.append([arg_name.strip(), arg_type.strip(), default_value.strip()])
            
            current_function = {
                "function_name": func_name,
                "arguments": function_arguments,
                "return_value": return_value,
                "documentation": "",
            }
            inside_function = True

        elif stripped_line.startswith(('enum ', 'const ', 'var ')):
            if inside_function or inside_class:
                continue
            if not first_member_found:
                first_member_found = True
            process_member()
            
            member_def = stripped_line.split(' ', 1)
            if len(member_def) < 2:
                continue
            
            member_prefix = member_def[0].strip()
            member_data = member_def[1].strip()
            
            member_type = ''
            if ':=' in member_data:
                name, value = member_data.split(':=', 1)
                name = name.strip()
                value = value.strip()
                member_type = infer_type_from_value(value)
            elif ':' in member_data:
                name, type_and_value = member_data.split(':', 1)
                type_and_value = type_and_value.strip()
                type_end = type_and_value.find(' ')
                if type_end == -1:
                    type_end = len(type_and_value)
                possible_type = type_and_value[:type_end].strip()
                member_type = possible_type  # Keep whatever type is specified
                value = type_and_value[type_end:].strip()
                name = name.strip()
            elif '=' in member_data:
                name, value = member_data.split('=', 1)
                name = name.strip()
                value = value.strip()
                member_type = ''  # Leave type blank if not specified
            else:
                name = member_data
                value = ''
                member_type = 'unknown'  # Use 'unknown' if type cannot be inferred and := is not used
            
            if name.startswith('_'):
                continue
            
            current_member = {
                "name": name,
                "type": member_type,
                "member_prefix": member_prefix,
                "value": value
            }

        elif stripped_line.startswith('signal '):
            process_current_signal()
            
            signal_def = stripped_line[7:]
            signal_name_end = signal_def.find('(')
            signal_name = signal_def[:signal_name_end].strip()
            
            args_start = signal_name_end + 1
            args_end = signal_def.find(')')
            args_part = signal_def[args_start:args_end].strip()
            
            signal_arguments = []
            if args_part:
                args_list = args_part.split(',')
                for arg in args_list:
                    arg = arg.strip()
                    if arg:
                        signal_arguments.append(arg)
            
            current_signal = {
                "signal_name": signal_name,
                "signal_arguments": signal_arguments,
                "signal_documentation": "",
            }

        elif stripped_line.startswith('class '):
            if inside_class:
                continue
            process_member()
            process_current_signal()
            inside_class = True
            class_name = stripped_line[6:].strip()
        
        elif stripped_line.startswith('extends '):
            parent_class = stripped_line[8:].strip()

    process_current_function()
    process_member()
    process_current_signal()

    return {
        "function_documentation": functions,
        "member_documentation": members,
        "signal_documentation": signals,
        "class_documentation": " ".join(class_documentation).strip(),
        "class_name": class_name,
        "parent_class": parent_class,
        "script_name": script_name
    }

def generate_markdown(parsed_data):
    class_name = parsed_data["class_name"]
    script_name = parsed_data["script_name"]
    parent_class = parsed_data["parent_class"]
    class_documentation = parsed_data["class_documentation"]

    members = parsed_data["member_documentation"]
    signals = parsed_data["signal_documentation"]
    functions = parsed_data["function_documentation"]

    markdown = f"# {class_name}\n\n"
    if class_documentation:
        markdown += f"## Class Documentation\n{class_documentation}\n\n"
    
    if parent_class:
        markdown += f"**Extends**: {parent_class}\n\n"

    if members:
        markdown += "## Members\n"
        for member in members:
            prefix = member["member_prefix"] if member["member_prefix"] else ''
            markdown += f"- **{prefix}{member['member_name']}** ({member['member_type']})"
            if member["member_value"]:
                markdown += f" = {member['member_value']}"
            if member["documentation"]:
                markdown += f": {member['documentation']}"
            markdown += "\n"
    
    if signals:
        markdown += "## Signals\n"
        for signal in signals:
            signal_args = ", ".join(signal["signal_arguments"])
            markdown += f"- **{signal['signal_name']}**({signal_args})"
            if signal["signal_documentation"]:
                markdown += f": {signal['signal_documentation']}"
            markdown += "\n"
    
    if functions:
        markdown += "## Functions\n"
        for function in functions:
            args = ", ".join([f"{arg[0]}: {arg[1]}" for arg in function["arguments"]])
            return_type = f" -> {function['return_value']}" if function["return_value"] else ''
            markdown += f"- **{function['function_name']}**({args}){return_type}"
            if function["documentation"]:
                markdown += f": {function['documentation']}"
            markdown += "\n"

    return markdown

# Example usage:
parsed_data = parse_gdscript_file(TEST_FILE_PATH)
markdown_output = generate_markdown(parsed_data)
print(markdown_output)



# output = parse_gdscript_file(TEST_FILE_PATH)
# for k in output.keys():
#     print(f"\n{k}: {output[k]}")

# for k in output["member_documentation"]:
#     print(k)

