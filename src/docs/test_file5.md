# GodotGlobalLogExample    
**Extends** Node
        
This script defines a global logging system for a Godot application. It manages logging for various severity levels, such as critical errors, warnings, and informational messages. The logger allows for controlling which objects are permitted to log messages and whether logs should be output to the console or stored for later retrieval. Additionally, the logger can handle elevated logging for debugging purposes, and it supports tracking and storing log records for different objects.  

The class includes mechanisms to control logging permissions on a per-object basis and to configure how logs are output or stored. Log messages are formatted according to predefined templates and include details such as the time, caller, and message type. 





---
# Properties
| | Property Name | Property Type | Property Default Value |
| --- | :--- | :---: | ---: |
| enum | **[CODE](#enum-code)** | *enum* | UNDEFINED, CRITICAL, ERROR, WARNING, INFO |
| const | **[STARTUP_LOG_FSTRING](#const-startup_log_fstring)** | *string* | "[{device}] Logger service ready @ {time}" |
| const | **[LOG_FSTRING](#const-log_fstring)** | *string* | "[t{time}] {caller}t[{type}] | {message}" |
| @export var | **[record_logs](#export-var-record_logs)** | *bool* | true |
| var | **[allow_log_output](#var-allow_log_output)** | *bool* | true |
| var | **[allow_log_registration](#var-allow_log_registration)** | *bool* | true |
| var | **[total_log_calls](#var-total_log_calls)** | *int* | 0 |
| var | **[total_log_output](#var-total_log_output)** | *int* | 0 |
| var | **[log_register](#var-log_register)** | ** | {} |
| var | **[log_permissions](#var-log_permissions)** | ** | {} |
| var | **[_log_permissions_last_state](#var-_log_permissions_last_state)** | ** | {} |


---
## ENUMS
### enum CODE
- **type:** enum

- *[default value = undefined, critical, error, warning, info]*

Enumerated log codes to define the severity levels of log messages



---
## CONSTANTS
### const STARTUP_LOG_FSTRING
- **type:** string

- *[default value = "[{device}] logger service ready @ {time}"]*

Constant string format for the initial startup log message
### const LOG_FSTRING
- **type:** string

- *[default value = "[t{time}] {caller}t[{type}] | {message}"]*

Constant string format for general log messages



---
## EXPORTS
### @export var record_logs
- **type:** bool

- *[default value = true]*

Variable to control whether logs should be recorded in the log register



---
## PUBLIC_VARS
### var allow_log_output
- **type:** bool

- *[default value = true]*

Variable to control whether logs should be output to the console
### var allow_log_registration
- **type:** bool

- *[default value = true]*

Variable to control whether logs should be stored in the log register
### var total_log_calls
- **type:** int

- *[default value = 0]*

Counter to track the total number of log calls made during runtime
### var total_log_output
- **type:** int

- *[default value = 0]*

Counter to track the total number of logs that were output to the console
### var log_register
- *[default value = {}]*

Dictionary to store logs associated with each object
### var log_permissions
- *[default value = {}]*

Dictionary to store logging permissions for each object



---
## PRIVATE_VARS
### var _log_permissions_last_state
- *[default value = {}]*

Dictionary to store the last state of log permissions for objects, used to revert permissions if needed






---
## PUBLIC_FUNCS
### (void) func critical
{func_arg_string}

Function to log a critical error message Critical logs indicate severe issues that require program termination Arguments: arg_caller: The object making the log call arg_error_message: The error message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) func debug_critical
{func_arg_string}

Function to log a critical error message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The error message to log
### (void) func error
{func_arg_string}

Function to log an error message Arguments: arg_caller: The object making the log call arg_error_message: The error message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) func debug_error
{func_arg_string}

Function to log an error message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The error message to log
### (void) func info
{func_arg_string}

Function to log an informational message Arguments: arg_caller: The object making the log call arg_error_message: The message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) func debug_info
{func_arg_string}

Function to log an informational message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The message to log
### (void) func warning
{func_arg_string}

Function to log a warning message Arguments: arg_caller: The object making the log call arg_error_message: The warning message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) func debug_warning
{func_arg_string}

Function to log a warning message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The warning message to log
### (bool) func get_permission
{func_arg_string}

Function to check if logging is permitted for a caller Determines whether logs from the caller should be processed based on permissions Arguments: arg_caller: The object requesting permission to log Returns: true if logging is permitted, false otherwise
### (int) func reset_permission
{func_arg_string}

Function to reset the logging permission for a caller to the previous state Arguments: arg_caller: The object whose permission should be reset Returns: OK if the permission was reset successfully, ERR_INVALID_PARAMETER if not
### (void) func set_permission_default
{func_arg_string}

Function to set the default logging permission for a caller Arguments: arg_caller: The object whose permission should be set to default arg_store_permission: If true, stores the current permission before changing
### (void) func set_permission_disabled
{func_arg_string}

Function to disable logging permission for a caller Arguments: arg_caller: The object whose logging permission should be disabled arg_store_permission: If true, stores the current permission before changing
### (void) func set_permission_elevated
{func_arg_string}

Function to elevate logging permission for a caller Elevated permissions allow the caller to log additional messages Arguments: arg_caller: The object whose logging permission should be elevated arg_store_permission: If true, stores the current permission before changing
### (void) func store_permission
{func_arg_string}

Function to store the current logging permission for a caller Arguments: arg_caller: The object whose permission state should be stored



---
## PRIVATE_FUNCS
### (unspecified) func _ready
{func_arg_string}

Function called when the node is added to the scene Initializes the logger, prevents automatic quit, and logs startup information
### (void) func _change_permission
{func_arg_string}

Internal function to change logging permission for a caller Arguments: arg_caller: The object whose logging permission should be changed arg_permission: The new permission value (true, false, or null)
### (bool) func _check_log_permission
{func_arg_string}

Internal function to check if logging is permitted for a caller Ensures that the caller has permission to log before proceeding Arguments: arg_caller: The object requesting to log arg_show_on_elevated_only: If true, only allows logging if the caller has elevated permissions Returns: true if logging is permitted, false otherwise
### (void) func _log
{func_arg_string}

Internal function to handle all logging operations Constructs and stores the log record, and outputs it if permitted Arguments: arg_caller: The object making the log call arg_log_message: The message to log arg_log_code_id: The severity level of the log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (unspecified) func _on_logger_startup
{func_arg_string}

Function to log the initial startup message when the logger is initialized Gathers system information and logs it to indicate the logger is ready
### (void) func _output_log
{func_arg_string}

Internal function to output a log record to the console Prints the log message to the console if allowed, and tracks output count Arguments: arg_log_record: The log record to output
### (void) func _register_log
{func_arg_string}

Internal function to store a log record in the log register Adds the log record to the appropriate entry in the register if allowed Arguments: arg_caller: The object making the log call arg_log_record: The log record to store



---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*