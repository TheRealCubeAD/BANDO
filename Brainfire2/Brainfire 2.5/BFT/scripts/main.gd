extends Node2D

export var room_size = 16
export var wall_treshold = 0.4

var cur_scene
var new_scene

var player


func _enter_tree():
	# checking room size
	if room_size % 2 == 1 or room_size < 6 or room_size > 20:
		print_debug("INVALID ROOM_SIZE")
		get_tree().quit()


func _ready():
	# for testing
	cur_scene = load("res://room.tscn").instance()
	cur_scene.set_name("room 1")
	get_node("room_layer").add_child(cur_scene)
	
	# init player
	player = get_node("player")
	player.set_pos(Vector2(0, room_size/2 - 1))


func _input(event):
	if event.is_action_pressed("key_esc"):
		get_tree().quit()
