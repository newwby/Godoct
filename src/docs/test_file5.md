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
# Functions

| | Function Name | Function Arguments | Function Return Value |
| --- | :--- | :--- | ---: |
| public | **[critical](#void-critical)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[debug_critical](#void-debug_critical)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[error](#void-error)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[debug_error](#void-debug_error)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[info](#void-info)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[debug_info](#void-debug_info)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[warning](#void-warning)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[debug_warning](#void-debug_warning)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[get_permission](#bool-get_permission)** | arg_caller: Object<br> | bool
| public | **[reset_permission](#int-reset_permission)** | arg_caller: Object<br> | int
| public | **[set_permission_default](#void-set_permission_default)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[set_permission_disabled](#void-set_permission_disabled)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[set_permission_elevated](#void-set_permission_elevated)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[store_permission](#void-store_permission)** | arg_caller: Object<br> | void
| private | **[_ready](#void-_ready)** |  | void
| private | **[_change_permission](#void-_change_permission)** | arg_caller: Object<br>arg_permission<br> | void
| private | **[_check_log_permission](#bool-_check_log_permission)** | arg_caller: Object<br>arg_show_on_elevated_only: bool = false<br> | bool
| private | **[_log](#void-_log)** | arg_caller: Object<br>arg_log_message<br>arg_log_code_id: int = 0<br>arg_show_on_elevated_only: bool = false<br> | void
| private | **[_on_logger_startup](#void-_on_logger_startup)** |  | void
| private | **[_output_log](#void-_output_log)** | arg_log_record: LogRecord<br> | void
| private | **[_register_log](#void-_register_log)** | arg_caller: Object<br>arg_log_record: LogRecord<br> | void



---
# Properties


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
## PUBLIC VARS
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
## PRIVATE VARS
### var _log_permissions_last_state
- *[default value = {}]*

Dictionary to store the last state of log permissions for objects, used to revert permissions if needed



---
# Functions


---
## PUBLIC FUNCS
### (void) critical
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**


Function to log a critical error message Critical logs indicate severe issues that require program termination Arguments: arg_caller: The object making the log call arg_error_message: The error message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) debug_critical
- **arg_caller: Object**
- **arg_error_message**


Function to log a critical error message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The error message to log
### (void) error
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**


Function to log an error message Arguments: arg_caller: The object making the log call arg_error_message: The error message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) debug_error
- **arg_caller: Object**
- **arg_error_message**


Function to log an error message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The error message to log
### (void) info
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**


Function to log an informational message Arguments: arg_caller: The object making the log call arg_error_message: The message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) debug_info
- **arg_caller: Object**
- **arg_error_message**


Function to log an informational message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The message to log
### (void) warning
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**


Function to log a warning message Arguments: arg_caller: The object making the log call arg_error_message: The warning message to log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) debug_warning
- **arg_caller: Object**
- **arg_error_message**


Function to log a warning message only if elevated logging is enabled Arguments: arg_caller: The object making the log call arg_error_message: The warning message to log
### (bool) get_permission
- **arg_caller: Object**


Function to check if logging is permitted for a caller Determines whether logs from the caller should be processed based on permissions Arguments: arg_caller: The object requesting permission to log Returns: true if logging is permitted, false otherwise
### (int) reset_permission
- **arg_caller: Object**


Function to reset the logging permission for a caller to the previous state Arguments: arg_caller: The object whose permission should be reset Returns: OK if the permission was reset successfully, ERR_INVALID_PARAMETER if not
### (void) set_permission_default
- **arg_caller: Object**
- **arg_store_permission: bool = false**


Function to set the default logging permission for a caller Arguments: arg_caller: The object whose permission should be set to default arg_store_permission: If true, stores the current permission before changing
### (void) set_permission_disabled
- **arg_caller: Object**
- **arg_store_permission: bool = false**


Function to disable logging permission for a caller Arguments: arg_caller: The object whose logging permission should be disabled arg_store_permission: If true, stores the current permission before changing
### (void) set_permission_elevated
- **arg_caller: Object**
- **arg_store_permission: bool = false**


Function to elevate logging permission for a caller Elevated permissions allow the caller to log additional messages Arguments: arg_caller: The object whose logging permission should be elevated arg_store_permission: If true, stores the current permission before changing
### (void) store_permission
- **arg_caller: Object**


Function to store the current logging permission for a caller Arguments: arg_caller: The object whose permission state should be stored



---
## PRIVATE FUNCS
### (void) _ready


Function called when the node is added to the scene Initializes the logger, prevents automatic quit, and logs startup information
### (void) _change_permission
- **arg_caller: Object**
- **arg_permission**


Internal function to change logging permission for a caller Arguments: arg_caller: The object whose logging permission should be changed arg_permission: The new permission value (true, false, or null)
### (bool) _check_log_permission
- **arg_caller: Object**
- **arg_show_on_elevated_only: bool = false**


Internal function to check if logging is permitted for a caller Ensures that the caller has permission to log before proceeding Arguments: arg_caller: The object requesting to log arg_show_on_elevated_only: If true, only allows logging if the caller has elevated permissions Returns: true if logging is permitted, false otherwise
### (void) _log
- **arg_caller: Object**
- **arg_log_message**
- **arg_log_code_id: int = 0**
- **arg_show_on_elevated_only: bool = false**


Internal function to handle all logging operations Constructs and stores the log record, and outputs it if permitted Arguments: arg_caller: The object making the log call arg_log_message: The message to log arg_log_code_id: The severity level of the log arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
### (void) _on_logger_startup


Function to log the initial startup message when the logger is initialized Gathers system information and logs it to indicate the logger is ready
### (void) _output_log
- **arg_log_record: LogRecord**


Internal function to output a log record to the console Prints the log message to the console if allowed, and tracks output count Arguments: arg_log_record: The log record to output
### (void) _register_log
- **arg_caller: Object**
- **arg_log_record: LogRecord**


Internal function to store a log record in the log register Adds the log record to the appropriate entry in the register if allowed Arguments: arg_caller: The object making the log call arg_log_record: The log record to store



---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*