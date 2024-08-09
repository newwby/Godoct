# test file    
**Extends** Node
        
this is the test documentation for the test file this line should be included in the test docs  

(another valid line for the test docs) 



---
# Signals

| | Signal Name | Signal Arguments |
| --- | :--- | ---: |
| signal | **[test_signal](#signal-test_signal)** | test_arg1, test_arg2
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
| static | **[critical](#void-critical)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[debug_critical](#void-debug_critical)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[debug_error](#void-debug_error)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[debug_info](#void-debug_info)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[debug_warning](#void-debug_warning)** | arg_caller: Object<br>arg_error_message<br> | void
| public | **[error](#void-error)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[get_permission](#bool-get_permission)** | arg_caller: Object<br> | bool
| public | **[info](#void-info)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| public | **[log_stack_trace](#void-log_stack_trace)** | arg_caller: Object<br> | void
| public | **[reset_permission](#int-reset_permission)** | arg_caller: Object<br> | int
| public | **[set_permission_default](#void-set_permission_default)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[set_permission_disabled](#void-set_permission_disabled)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[set_permission_elevated](#void-set_permission_elevated)** | arg_caller: Object<br>arg_store_permission: bool = false<br> | void
| public | **[store_permission](#void-store_permission)** | arg_caller: Object<br> | void
| public | **[warning](#void-warning)** | arg_caller: Object<br>arg_error_message<br>arg_show_on_elevated_only: bool = false<br> | void
| private | **[_ready](#void-_ready)** |  | void
| private | **[_change_permission](#void-_change_permission)** | arg_caller: Object<br>arg_permission<br> | void
| private | **[_is_permitted](#bool-_is_permitted)** | arg_log_caller: Object<br>arg_show_on_elevated_only: bool<br> | bool
| private | **[_log](#void-_log)** | arg_caller: Object<br>arg_error_message<br>arg_log_code: int = 0<br>arg_show_on_elevated_only: bool = false<br> | void
| private | **[_on_logger_startup](#void-_on_logger_startup)** |  | void
| private | **[_output_log](#void-_output_log)** | arg_next_log: LogRecord<br> | void
| private | **[_store_log](#void-_store_log)** | arg_log: LogRecord<br> | void


---
# Signals

---
# Properties


---
## SIGNALS
### signal test_signal
(**test_arg1**, **test_arg2**)

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
# Functions


---
## STATIC FUNCS
### (void) critical
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**


critical method docstring, multi-line documentation filtering test this should be three lines into one



---
## PUBLIC FUNCS
### (void) debug_critical
- **arg_caller: Object**
- **arg_error_message**


debug_critical documentation
### (void) debug_error
- **arg_caller: Object**
- **arg_error_message**

### (void) debug_info
- **arg_caller: Object**
- **arg_error_message**

### (void) debug_warning
- **arg_caller: Object**
- **arg_error_message**


debug ('elevated') logs only appear in the debugger/output/console if the object emitting the log has had their logging permissions elevated use debug/elevated logs to hide logs you only need when debugging
### (void) error
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**

### (bool) get_permission
- **arg_caller: Object**

### (void) info
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**

### (void) log_stack_trace
- **arg_caller: Object**

### (int) reset_permission
- **arg_caller: Object**

### (void) set_permission_default
- **arg_caller: Object**
- **arg_store_permission: bool = false**

### (void) set_permission_disabled
- **arg_caller: Object**
- **arg_store_permission: bool = false**

### (void) set_permission_elevated
- **arg_caller: Object**
- **arg_store_permission: bool = false**

### (void) store_permission
- **arg_caller: Object**

### (void) warning
- **arg_caller: Object**
- **arg_error_message**
- **arg_show_on_elevated_only: bool = false**




---
## PRIVATE FUNCS
### (void) _ready


_ready documentation
### (void) _change_permission
- **arg_caller: Object**
- **arg_permission**

### (bool) _is_permitted
- **arg_log_caller: Object**
- **arg_show_on_elevated_only: bool**

### (void) _log
- **arg_caller: Object**
- **arg_error_message**
- **arg_log_code: int = 0**
- **arg_show_on_elevated_only: bool = false**

### (void) _on_logger_startup

### (void) _output_log
- **arg_next_log: LogRecord**

### (void) _store_log
- **arg_log: LogRecord**




---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*