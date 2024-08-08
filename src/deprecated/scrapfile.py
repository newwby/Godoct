import re

def strip_whitespace(signature: str) -> str:
    # Replace multiple whitespace characters (spaces, tabs) with a single space
    cleaned_signature = re.sub(r'[ \t]+', ' ', signature)
    return cleaned_signature

# Function signature as a string
signature = """
func _log(              
    arg_caller: Object,             
    arg_error_message,              
    arg_log_code: int = 0,          
    arg_show_on_elevated_only: bool = false         
) -> void:
"""

# Clean up the signature
cleaned_signature = re.sub(r'[ \t]+', ' ', signature)
sigs = [cleaned_signature.replace("\n", "")]
print(sigs)