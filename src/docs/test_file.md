# TEST_FILE    
**Extends** Node
        
this is the test documentation for the test file this line should be included in the test docs  

(another valid line for the test docs) 


# Properties


---
## ENUMS
| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| **CODE** | *enum* | UNDEFINED, CRITICAL, ERROR, WARNING, INFO |

### CODE
- **type:** enum

- *[default value = undefined, critical, error, warning, info]*



---
## CONSTANTS
| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| **STARTUP_LOG_FSTRING** | *string* | "[{device}] Logger service ready @ {time}" |
| **LOG_FSTRING** | *string* | "[t{time}] {caller}t[{type}] | {message}" |

### STARTUP_LOG_FSTRING
- **type:** string

- *[default value = "[{device}] logger service ready @ {time}"]*
### LOG_FSTRING
- **type:** string

- *[default value = "[t{time}] {caller}t[{type}] | {message}"]*



---
## EXPORT VARS
| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| **record_logs** | *bool* | true |

### record_logs
- **type:** bool

- *[default value = true]*

record logs documentation



---
## PUBLIC VARS
| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| **allow_log_output** | *bool* | true |
| **allow_log_registration** | *bool* | true |
| **total_log_calls** | *int* | 0 |
| **total_log_output** | *int* | 0 |
| **log_register** | ** | {} |
| **log_permissions** | ** | {} |

### allow_log_output
- **type:** bool

- *[default value = true]*
### allow_log_registration
- **type:** bool

- *[default value = true]*
### total_log_calls
- **type:** int

- *[default value = 0]*

log call not output documentation
### total_log_output
- **type:** int

- *[default value = 0]*

log output documentation
### log_register
- *[default value = {}]*

documentation for log_register
### log_permissions
- *[default value = {}]*

multi-line variable declaration test here's the second line for the multi-line variable declaration test



---
## PRIVATE VARS
| Property Name | Property Type | Propery Default Value |
| --- | :---: | ---: |
| **_log_permissions_last_state** | ** | {} |

### _log_permissions_last_state
- *[default value = {}]*

documentation for _log_permission_last_state


