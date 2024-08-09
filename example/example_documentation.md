# WeatherController   
**Extends** Node
        
This script is an example of a fictional "WeatherController" for a game or simulation. The WeatherController manages different weather states such as clear, rainy, and stormy, and handles transitions between these states. It includes functions to manually set weather, randomize weather, and adjust intensity. Properties include current weather state, weather intensity, and transition speed. This script is designed to be attached to a Node that will serve as the central controller for all weather-related effects in the scene. 



---
# Signals

| | Signal Name | Signal Arguments |
| --- | :--- | ---: |
| signal | **[weather_state_changed](#signal-weather_state_changed)** | new_state: int
---
# Properties
| | Property Name | Property Type | Property Default Value |
| --- | :--- | :---: | ---: |
| enum | **[WEATHER_STATE](#enum-weather_state)** | *enum* | CLEAR, RAINY, STORMY |
| @export var | **[initial_weather_state](#export-var-initial_weather_state)** | *int* | WEATHER_STATE.CLEAR |
| var | **[current_weather_state](#var-current_weather_state)** | *int* | initial_weather_state |
| var | **[weather_intensity](#var-weather_intensity)** | ** | 50 |
| var | **[transition_speed](#var-transition_speed)** | *float* | 1.0 |
| var | **[transition_timer](#var-transition_timer)** | *Timer* |  |


---
# Functions

| | Function Name | Function Arguments | Function Return Value |
| --- | :--- | :--- | ---: |
| public | **[set_weather_state](#void-set_weather_state)** | new_state: int<br>intensity: addmethod! = 50<br> | void
| public | **[randomize_weather](#void-randomize_weather)** |  | void
| public | **[start_transition](#void-start_transition)** | new_state: int<br> | void
| public | **[adjust_intensity](#void-adjust_intensity)** | new_intensity: int<br> | void
| private | **[_ready](#void-_ready)** |  | void
| private | **[_on_transition_timer_timeout](#void-_on_transition_timer_timeout)** |  | void


---
# Signals


---
## SIGNALS
### signal weather_state_changed
(**new_state: int**)

Signal emitted when the weather state changes Connected functions can respond to the new weather state



---
# Properties


---
## ENUMS
### enum WEATHER_STATE
- **type:** enum

- *[default value = clear, rainy, stormy]*

Enumerated weather states to define possible weather conditions



---
## EXPORTS
### @export var initial_weather_state
- **type:** int

- *[default value = weather_state.clear]*

Exported property to control the initial weather state The weather state can be set to CLEAR, RAINY, or STORMY



---
## PUBLIC VARS
### var current_weather_state
- **type:** int

- *[default value = initial_weather_state]*

Property to store the current weather state This will change as weather transitions occur
### var weather_intensity
- *[default value = 50]*

Property to control the intensity of the current weather Ranges from 0 (no intensity) to 100 (maximum intensity)
### var transition_speed
- **type:** float

- *[default value = 1.0]*

Property to control the speed of weather transitions Speed is defined as the time it takes to fully transition from one state to another
### var transition_timer
- **type:** timer

Timer to manage weather transitions The timer is used internally to trigger changes in weather state



---
# Functions


---
## PUBLIC FUNCS
### (void) set_weather_state
- **new_state: int**
- **intensity: addmethod! = 50**


Function to set the weather to a specific state Immediately changes the weather to the specified state and resets intensity Arguments: new_state: The weather state to change to (CLEAR, RAINY, STORMY) intensity: The intensity of the new weather state (default is 50)
### (void) randomize_weather


Function to randomize the weather state Randomly selects a weather state and sets it with a random intensity
### (void) start_transition
- **new_state: int**


Function to start a gradual transition to a new weather state Begins the transition process which will occur over the set transition speed Arguments: new_state: The weather state to transition to (CLEAR, RAINY, STORMY)
### (void) adjust_intensity
- **new_intensity: int**


Function to adjust the intensity of the current weather Changes the intensity without altering the current weather state Arguments: new_intensity: The new intensity level (0 to 100)



---
## PRIVATE FUNCS
### (void) _ready


Function called when the node is added to the scene Initializes the weather controller by setting up the transition timer and starting the initial weather state
### (void) _on_transition_timer_timeout


Internal function called when the transition timer times out Completes the transition to the new weather state



---
*Documentation generated with [Godoct](https://github.com/newwby/Godoct)*