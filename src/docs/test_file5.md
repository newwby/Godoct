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
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*