# DataUtility    
**Extends** Node
        






---
# Properties
| | Property Name | Property Type | Property Default Value |
| --- | :--- | :---: | ---: |
| const | **[LOCAL_PATH](#const-local_path)** | *string* | "res://" |
| const | **[USER_PATH](#const-user_path)** | *string* | "user://" |
| const | **[BACKUP_SUFFIX](#const-backup_suffix)** | *string* | "_backup" |
| const | **[TEMP_SUFFIX](#const-temp_suffix)** | *string* | "_temp" |
| const | **[EXT_RESOURCE](#const-ext_resource)** | *string* | ".tres" |


---
## CONSTANTS
### const LOCAL_PATH
- **type:** string

- *[default value = "res://"]*
### const USER_PATH
- **type:** string

- *[default value = "user://"]*
### const BACKUP_SUFFIX
- **type:** string

- *[default value = "_backup"]*
### const TEMP_SUFFIX
- **type:** string

- *[default value = "_temp"]*
### const EXT_RESOURCE
- **type:** string

- *[default value = ".tres"]*






---
## STATIC_FUNCS
### (String) static func clean_file_name
{func_arg_string}
### (PackedStringArray) static func get_dir_names_recursive
{func_arg_string}
### (Array) static func get_dir_paths
{func_arg_string}
### (PackedStringArray) static func get_file_names
{func_arg_string}
### (PackedStringArray) static func get_file_paths
{func_arg_string}
### (Error) static func save_resource
{func_arg_string}

if arg_backup is specified, any previous file found will be moved to a separate file with the 'BACKUP_SUFFIX' added to its file name
### (bool) static func validate_directory
{func_arg_string}



---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*