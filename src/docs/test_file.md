# test file    
**Extends** Node
        
this is the test documentation for the test file this line should be included in the test docs  

(another valid line for the test docs) 



---
# Signals

| | Signal Name | Signal Arguments |
| --- | :--- | ---: |
| signal | **[test_signal](#signal-test_signal)** | (test_arg1, test_arg2)

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
## SIGNALS
### signal test_signal
(test_arg1, test_arg2)

signal documentation



---
## ENUMS
### enum CODE
- **type:** enum

- *[default value = undefined, critical, error, warning, info]*



---
## CONSTANTS
### const STARTUP_LOG_FSTRING
- **type:** string

- *[default value = "[{device}] logger service ready @ {time}"]*
### const LOG_FSTRING
- **type:** string

- *[default value = "[t{time}] {caller}t[{type}] | {message}"]*



---
## EXPORTS
### @export var record_logs
- **type:** bool

- *[default value = true]*

record logs documentation



---
## PUBLIC VARS
### var allow_log_output
- **type:** bool

- *[default value = true]*
### var allow_log_registration
- **type:** bool

- *[default value = true]*
### var total_log_calls
- **type:** int

- *[default value = 0]*

log call not output documentation
### var total_log_output
- **type:** int

- *[default value = 0]*

log output documentation
### var log_register
- *[default value = {}]*

documentation for log_register
### var log_permissions
- *[default value = {}]*

multi-line variable declaration test here's the second line for the multi-line variable declaration test



---
## PRIVATE VARS
### var _log_permissions_last_state
- *[default value = {}]*

documentation for _log_permission_last_state






---
## STATIC FUNCS
### (void) static func critical
- arg_caller: Object
- arg_error_message
- arg_show_on_elevated_only: bool = false


critical method docstring, multi-line documentation filtering test this should be three lines into one



---
## PUBLIC FUNCS
### (void) func debug_critical
- arg_caller: Object
- arg_error_message


debug_critical documentation
### (void) func debug_error
- arg_caller: Object
- arg_error_message

### (void) func debug_info
- arg_caller: Object
- arg_error_message

### (void) func debug_warning
- arg_caller: Object
- arg_error_message


debug ('elevated') logs only appear in the debugger/output/console if the object emitting the log has had their logging permissions elevated use debug/elevated logs to hide logs you only need when debugging
### (void) func error
- arg_caller: Object
- arg_error_message
- arg_show_on_elevated_only: bool = false

### (bool) func get_permission
- arg_caller: Object

### (void) func info
- arg_caller: Object
- arg_error_message
- arg_show_on_elevated_only: bool = false

### (void) func log_stack_trace
- arg_caller: Object

### (int) func reset_permission
- arg_caller: Object

### (void) func set_permission_default
- arg_caller: Object
- arg_store_permission: bool = false

### (void) func set_permission_disabled
- arg_caller: Object
- arg_store_permission: bool = false

### (void) func set_permission_elevated
- arg_caller: Object
- arg_store_permission: bool = false

### (void) func store_permission
- arg_caller: Object

### (void) func warning
- arg_caller: Object
- arg_error_message
- arg_show_on_elevated_only: bool = false




---
## PRIVATE FUNCS
### (void) func _ready


_ready documentation
### (void) func _change_permission
- arg_caller: Object
- arg_permission

### (bool) func _is_permitted
- arg_log_caller: Object
- arg_show_on_elevated_only: bool

### (void) func _log
- arg_caller: Object
- arg_error_message
- arg_log_code: int = 0
- arg_show_on_elevated_only: bool = false

### (void) func _on_logger_startup

### (void) func _output_log
- arg_next_log: LogRecord

### (void) func _store_log
- arg_log: LogRecord




---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*