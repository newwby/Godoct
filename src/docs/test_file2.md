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
## STATIC FUNCS
### (String) static func clean_file_name
- arg_file_name: String
- arg_replace_char: String = ""
- arg_replace_spaces: bool = true
- arg_to_lowercase: bool = true

### (PackedStringArray) static func get_dir_names_recursive
- arg_directory_path: String

### (Array) static func get_dir_paths
- arg_directory_path: String
- arg_get_recursively: bool = false

### (PackedStringArray) static func get_file_names
- arg_directory_path: String
- arg_is_recursive: bool = true

### (PackedStringArray) static func get_file_paths
- arg_directory_path: String
- arg_is_recursive: bool = true

### (Error) static func save_resource
- arg_saveable_res: Resource
- arg_file_path: String
- arg_backup: bool = false


if arg_backup is specified, any previous file found will be moved to a separate file with the 'BACKUP_SUFFIX' added to its file name
### (bool) static func validate_directory
- arg_directory_path: String




---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*