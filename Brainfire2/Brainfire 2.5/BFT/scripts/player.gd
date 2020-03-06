extends Sprite

var moving
var destination
export var speed = 1500

var game

func _ready():
	game = get_parent()
	moving = false


func set_pos(new_pos):  # set absolute position
	position = new_pos * 200
	destination = new_pos


func _process(delta):
	# move player if needed
	var real_dest = destination * 200
	if real_dest != position:
		moving = true
		if (real_dest - position).length() < 10:
			position = real_dest
		else:
			position += (real_dest - position).normalized() * speed * delta
	else:
		moving = false


func _input(event):
	# react to arrow-keys
	if not moving:
		if event.is_action_pressed("key_up"):
			destination = game.cur_scene.run(destination, Vector2(0, -1))
		elif event.is_action_pressed("key_down"):
			destination = game.cur_scene.run(destination, Vector2(0, 1))
		elif event.is_action_pressed("key_left"):
			destination = game.cur_scene.run(destination, Vector2(-1, 0))
		elif event.is_action_pressed("key_right"):
			destination = game.cur_scene.run(destination, Vector2(1, 0))
		
