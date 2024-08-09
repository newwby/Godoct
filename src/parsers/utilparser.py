# takes a gdscript property or argument (e.g. varname := true, or varname: bool = true) and returns the pieces
def categorise_property(arg_property):
    var_name = ""
    var_default = ""
    var_type = ""

    # if inferred type from default arg
    if ":=" in arg_property:
        property_split = arg_property.split(":=")
        var_name = property_split[0].strip()
        var_default = property_split[1].strip()
        var_type = infer_type(var_default)
    else:
        # get specified type and default arg
        if ":" in arg_property and "=" in arg_property:
            property_split = arg_property.split(":")
            var_name = property_split[0]
            property_split[1] = property_split[1].split("=")
            var_type = property_split[1][0]
            var_default = property_split[1][1]
        
        # get specified type and ignore default arg
        elif ":" in arg_property and not "=" in arg_property:
            property_split = arg_property.split(":")
            var_name = property_split[0]
            var_type = property_split[1]
        
        # get default arg ignore specified type
        elif "=" in arg_property and not ":" in arg_property:
            property_split = arg_property.split("=")
            var_name = property_split[0]
            var_default = property_split[1]
        
        # ignore default and type
        else:
            var_name = arg_property
    
    return (var_name.strip(), var_type.strip(), var_default.strip())


def infer_type(arg_string):
    arg_string = str(arg_string)
    if "\"" in arg_string:
        return "string"
    elif arg_string == "true" or arg_string == "false":
        return "bool"
    elif "." in arg_string:
        return "float"
    elif "[" in arg_string:
        return "array"
    elif "{" in arg_string:
        return "dictionary"
    elif str(arg_string).isnumeric:
        return "int"
    elif arg_string[1:].isnumeric:
        return "int"
    else:
        return "unknown"

