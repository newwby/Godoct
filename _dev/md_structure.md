# This is a test file to simulate markdown formats for the generator script

---

# TEST_FILE
**Extends** Node

this is the test documentation for the test file this line should be included in the test docs

(another valid line for the test docs)

# Index.md
// Need to generate table of contents on index.md

# Doc for .gd file

# {class_name} or {script_name}
**Tool Script** //only show if {is_tool}

**Extends** {class_parent}

{class_documentation}

# Properties

## Var
//Var/Signal/Enum/Const
// may need special handling for signal/enum

| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| {name} | {type} | {default_value} |

//make sure to exclude empty values
### {name}
{docs}
- **Type:** {type}
- **Default Value**: {default_value}

## Functions
//Static Functions, Private Functions, Public Functions
//make sure to exclude any heading where they're empty

| Function Name | Function Arguments | Function Return Value |
| --- | :---: | ---: |
| {name} | {arguments_as_string}<br> {arg1, <br> arg2} | {return_value} |

// {arguments_as_string} needs to build a list of arguments reading {name}: {type} = {default} per argument, excluding the type/default if not present
// each new argument should be a new line using <br>

//make sure to exclude empty values
### {return value} {name}
{docs}
- **Argument** //repeat per argument, using same arguments_as_string format
