extends Node

## <class_doc>
## This script is an example of a fictional "WeatherController" for a game or simulation.
## The WeatherController manages different weather states such as clear, rainy, and stormy,
## and handles transitions between these states. 
## It includes functions to manually set weather, randomize weather, and adjust intensity.
## Properties include current weather state, weather intensity, and transition speed.
## This script is designed to be attached to a Node that will serve as the central controller 
## for all weather-related effects in the scene.

## Enumerated weather states to define possible weather conditions
enum WEATHER_STATE {CLEAR, RAINY, STORMY}

## Exported property to control the initial weather state
## The weather state can be set to CLEAR, RAINY, or STORMY
@export var initial_weather_state: int = WEATHER_STATE.CLEAR

## Property to store the current weather state
## This will change as weather transitions occur
var current_weather_state: int = initial_weather_state

## Property to control the intensity of the current weather
## Ranges from 0 (no intensity) to 100 (maximum intensity)
var weather_intensity = 50

## Property to control the speed of weather transitions
## Speed is defined as the time it takes to fully transition from one state to another
var transition_speed: float = 1.0

## Timer to manage weather transitions
## The timer is used internally to trigger changes in weather state
var transition_timer: Timer

## Signal emitted when the weather state changes
## Connected functions can respond to the new weather state
signal weather_state_changed(new_state: int)

## Function called when the node is added to the scene
## Initializes the weather controller by setting up the transition timer
## and starting the initial weather state
func _ready() -> void:
    transition_timer = Timer.new()
    add_child(transition_timer)
    transition_timer.set_wait_time(transition_speed)
    transition_timer.connect("timeout", self, "_on_transition_timer_timeout")
    set_weather_state(initial_weather_state)

## Function to set the weather to a specific state
## Immediately changes the weather to the specified state and resets intensity
## Arguments:
##   new_state: The weather state to change to (CLEAR, RAINY, STORMY)
##   intensity: The intensity of the new weather state (default is 50)
func set_weather_state(new_state: int, intensity := 50) -> void:
    current_weather_state = new_state
    weather_intensity = intensity
    emit_signal("weather_state_changed", new_state)
    print("Weather changed to {0} with intensity {1}".format([new_state, intensity]))

## Function to randomize the weather state
## Randomly selects a weather state and sets it with a random intensity
func randomize_weather() -> void:
    var new_state = randi() % 3
    var new_intensity = randi() % 101
    set_weather_state(new_state, new_intensity)

## Function to start a gradual transition to a new weather state
## Begins the transition process which will occur over the set transition speed
## Arguments:
##   new_state: The weather state to transition to (CLEAR, RAINY, STORMY)
func start_transition(new_state: int) -> void:
    transition_timer.start()
    current_weather_state = new_state
    print("Starting transition to weather state {0}".format([new_state]))

## Internal function called when the transition timer times out
## Completes the transition to the new weather state
func _on_transition_timer_timeout() -> void:
    set_weather_state(current_weather_state)
    transition_timer.stop()

## Function to adjust the intensity of the current weather
## Changes the intensity without altering the current weather state
## Arguments:
##   new_intensity: The new intensity level (0 to 100)
func adjust_intensity(new_intensity: int) -> void:
    weather_intensity = clamp(new
