# TEST_FILE    
**Extends** Node
        
this is the test documentation for the test file this line should be included in the test docs  

(another valid line for the test docs) 


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
## PUBLIC_VARS
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
## PRIVATE_VARS
### var _log_permissions_last_state
- *[default value = {}]*

documentation for _log_permission_last_state



---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*