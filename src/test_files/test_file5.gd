extends Node

class_name GodotGlobalLogExample

## <class_doc>
## This script defines a global logging system for a Godot application.
## It manages logging for various severity levels, such as critical errors,
## warnings, and informational messages. The logger allows for controlling
## which objects are permitted to log messages and whether logs should be
## output to the console or stored for later retrieval. 
## Additionally, the logger can handle elevated logging for debugging purposes,
## and it supports tracking and storing log records for different objects.
## 
## The class includes mechanisms to control logging permissions on a per-object
## basis and to configure how logs are output or stored. Log messages are 
## formatted according to predefined templates and include details such as the 
## time, caller, and message type.

## Enumerated log codes to define the severity levels of log messages
enum CODE {UNDEFINED, CRITICAL, ERROR, WARNING, INFO}

## Constant string format for the initial startup log message
const STARTUP_LOG_FSTRING := "[{device}] Logger service ready @ {time}"

## Constant string format for general log messages
const LOG_FSTRING := "[t{time}] {caller}\t[{type}] | {message}"

## Variable to control whether logs should be recorded in the log register
@export var record_logs := true

## Variable to control whether logs should be output to the console
var allow_log_output := true

## Variable to control whether logs should be stored in the log register
var allow_log_registration := true

## Counter to track the total number of log calls made during runtime
var total_log_calls := 0

## Counter to track the total number of logs that were output to the console
var total_log_output := 0

## Dictionary to store logs associated with each object
var log_register = {}

## Dictionary to store logging permissions for each object
var log_permissions = {}

## Dictionary to store the last state of log permissions for objects,
## used to revert permissions if needed
var _log_permissions_last_state = {}

## Inner class representing a single log record
## Contains details about the log, including the owner, timestamp, log type,
## message, and whether it was logged to the console
class LogRecord:
    var owner: Object
    var timestamp: int
    var log_code_id: int
    var log_code_name: String
    var log_message: String
    var logged_to_console: bool = false
    var full_log_string: String
    
    ## Constructor to initialize a log record with the provided details
    func _init(
            arg_owner: Object,
            arg_log_timestamp: int,
            arg_log_code_id: int,
            arg_log_code_name: String,
            arg_log_message: String,
            arg_log_string: String
            ):
        self.owner = arg_owner
        self.timestamp = arg_log_timestamp
        self.log_code_id = arg_log_code_id
        self.log_code_name = arg_log_code_name
        self.log_message = arg_log_message
        self.full_log_string = arg_log_string

## Function called when the node is added to the scene
## Initializes the logger, prevents automatic quit, and logs startup information
func _ready():
    get_tree().set_auto_accept_quit(false)
    _change_permission(self, true)
    _on_logger_startup()

## Function to log a critical error message
## Critical logs indicate severe issues that require program termination
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The error message to log
##   arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
func critical(
        arg_caller: Object,
        arg_error_message,
        arg_show_on_elevated_only: bool = false) -> void:
    _log(arg_caller, arg_error_message, 1, arg_show_on_elevated_only)

## Function to log a critical error message only if elevated logging is enabled
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The error message to log
func debug_critical(arg_caller: Object, arg_error_message) -> void:
    critical(arg_caller, arg_error_message, true)

## Function to log an error message
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The error message to log
##   arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
func error(
        arg_caller: Object,
        arg_error_message,
        arg_show_on_elevated_only: bool = false) -> void:
    _log(arg_caller, arg_error_message, 2, arg_show_on_elevated_only)

## Function to log an error message only if elevated logging is enabled
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The error message to log
func debug_error(arg_caller: Object, arg_error_message) -> void:
    error(arg_caller, arg_error_message, true)

## Function to log an informational message
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The message to log
##   arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
func info(
        arg_caller: Object,
        arg_error_message,
        arg_show_on_elevated_only: bool = false) -> void:
    _log(arg_caller, arg_error_message, 4, arg_show_on_elevated_only)

## Function to log an informational message only if elevated logging is enabled
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The message to log
func debug_info(arg_caller: Object, arg_error_message) -> void:
    info(arg_caller, arg_error_message, true)

## Function to log a warning message
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The warning message to log
##   arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
func warning(
        arg_caller: Object,
        arg_error_message,
        arg_show_on_elevated_only: bool = false) -> void:
    _log(arg_caller, arg_error_message, 3, arg_show_on_elevated_only)

## Function to log a warning message only if elevated logging is enabled
## Arguments:
##   arg_caller: The object making the log call
##   arg_error_message: The warning message to log
func debug_warning(arg_caller: Object, arg_error_message) -> void:
    warning(arg_caller, arg_error_message, true)

## Function to check if logging is permitted for a caller
## Determines whether logs from the caller should be processed based on permissions
## Arguments:
##   arg_caller: The object requesting permission to log
## Returns:
##   true if logging is permitted, false otherwise
func get_permission(arg_caller: Object) -> bool:
    var permission_allowed = true
    if arg_caller in log_permissions.keys():
        permission_allowed = log_permissions[arg_caller]
        if typeof(permission_allowed) != TYPE_BOOL:
            error(self, "invalid permission type for {0}".format([arg_caller]))
            return false
    return permission_allowed

## Function to reset the logging permission for a caller to the previous state
## Arguments:
##   arg_caller: The object whose permission should be reset
## Returns:
##   OK if the permission was reset successfully, ERR_INVALID_PARAMETER if not
func reset_permission(arg_caller: Object) -> int:
    if arg_caller in _log_permissions_last_state.keys():
        _change_permission(
                arg_caller, _log_permissions_last_state[arg_caller])
        _log_permissions_last_state.erase(arg_caller)
        return OK
    else:
        return ERR_INVALID_PARAMETER

## Function to set the default logging permission for a caller
## Arguments:
##   arg_caller: The object whose permission should be set to default
##   arg_store_permission: If true, stores the current permission before changing
func set_permission_default(
        arg_caller: Object,
        arg_store_permission: bool = false) -> void:
    if arg_store_permission:
        store_permission(arg_caller)
    _change_permission(arg_caller, null)

## Function to disable logging permission for a caller
## Arguments:
##   arg_caller: The object whose logging permission should be disabled
##   arg_store_permission: If true, stores the current permission before changing
func set_permission_disabled(
        arg_caller: Object,
        arg_store_permission: bool = false) -> void:
    if arg_store_permission:
        store_permission(arg_caller)
    _change_permission(arg_caller, false)

## Function to elevate logging permission for a caller
## Elevated permissions allow the caller to log additional messages
## Arguments:
##   arg_caller: The object whose logging permission should be elevated
##   arg_store_permission: If true, stores the current permission before changing
func set_permission_elevated(
        arg_caller: Object,
        arg_store_permission: bool = false) -> void:
    if arg_store_permission:
        store_permission(arg_caller)
    _change_permission(arg_caller, true)

## Function to store the current logging permission for a caller
## Arguments:
##   arg_caller: The object whose permission state should be stored
func store_permission(arg_caller: Object) -> void:
    if arg_caller in log_permissions.keys():
        _log_permissions_last_state[arg_caller] = log_permissions[arg_caller]
    else:
        _log_permissions_last_state[arg_caller] = null

## Internal function to change logging permission for a caller
## Arguments:
##   arg_caller: The object whose logging permission should be changed
##   arg_permission: The new permission value (true, false, or null)
func _change_permission(arg_caller: Object, arg_permission) -> void:
    log_permissions[arg_caller] = arg_permission

## Internal function to check if logging is permitted for a caller
## Ensures that the caller has permission to log before proceeding
## Arguments:
##   arg_caller: The object requesting to log
##   arg_show_on_elevated_only: If true, only allows logging if the caller has elevated permissions
## Returns:
##   true if logging is permitted, false otherwise
func _check_log_permission(
        arg_caller: Object,
        arg_show_on_elevated_only: bool = false) -> bool:
    var permission_allowed = true
    if not get_permission(arg_caller):
        return false
    if arg_show_on_elevated_only:
        permission_allowed = false
        if arg_caller in log_permissions.keys():
            permission_allowed = log_permissions[arg_caller] == true
    return permission_allowed

## Internal function to handle all logging operations
## Constructs and stores the log record, and outputs it if permitted
## Arguments:
##   arg_caller: The object making the log call
##   arg_log_message: The message to log
##   arg_log_code_id: The severity level of the log
##   arg_show_on_elevated_only: If true, only logs if the caller has elevated permissions
func _log(
        arg_caller: Object,
        arg_log_message,
        arg_log_code_id: int = 0,
        arg_show_on_elevated_only: bool = false) -> void:
    if not _check_log_permission(arg_caller, arg_show_on_elevated_only):
        return
    total_log_calls += 1
    var timestamp = Time.get_time_usec()
    var log_type_name = CODE.get_names()[arg_log_code_id]
    var log_message = LOG_FSTRING.format({
        "time": timestamp,
        "caller": arg_caller.to_string(),
        "type": log_type_name,
        "message": arg_log_message
    })
    var log_record = LogRecord.new(
            arg_caller, timestamp, arg_log_code_id,
            log_type_name, arg_log_message, log_message
    )
    _register_log(arg_caller, log_record)
    _output_log(log_record)

## Function to log the initial startup message when the logger is initialized
## Gathers system information and logs it to indicate the logger is ready
func _on_logger_startup():
    var current_time = OS.get_datetime(true)
    var time_formatted = str(current_time.hour).pad_zeros(2) + ":" + str(current_time.minute).pad_zeros(2)
    var system_model_name = OS.get_model_name()
    var os_name = OS.get_name()
    info(self, STARTUP_LOG_FSTRING.format({
        "device": "{0}/{1}".format([system_model_name, os_name]),
        "time": time_formatted
    }))

## Internal function to output a log record to the console
## Prints the log message to the console if allowed, and tracks output count
## Arguments:
##   arg_log_record: The log record to output
func _output_log(arg_log_record: LogRecord) -> void:
    if not allow_log_output:
        return
    print(arg_log_record.full_log_string)
    total_log_output += 1
    if arg_log_record.log_code_id == CODE.CRITICAL:
        assert(false)

## Internal function to store a log record in the log register
## Adds the log record to the appropriate entry in the register if allowed
## Arguments:
##   arg_caller: The object making the log call
##   arg_log_record: The log record to store
func _register_log(arg_caller: Object, arg_log_record: LogRecord) -> void:
    if not record_logs or not allow_log_registration:
        return
    if not (arg_caller in log_register):
        log_register[arg_caller] = []
    log_register[arg_caller].append(arg_log_record)
