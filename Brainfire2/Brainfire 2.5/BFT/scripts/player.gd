extends Node2D

var moving
var destination
export var speed = 1500

var rot_dest
export var rotation_speed = 700
var direction

var game
var sprite
var arm_left
var arm_right

func _ready():
	game = get_parent()
	sprite = get_node("player_sprite")
	arm_left = get_node("arm_left")
	arm_right = get_node("arm_right")
	arm_right.sin_offset = PI
	moving = false
	rot_dest = 90
	rotation_degrees = 90


func set_pos(new_pos):  # set absolute position
	position = new_pos * 200 + Vector2(100, 100)
	destination = new_pos


func _physics_process(delta):
	# move player if needed
	var real_dest = destination * 200 + Vector2(100, 100)
	if real_dest != position:
		if moving == false:
			arm_left.set_status("running")
			arm_right.set_status("running")
		moving = true
		if (real_dest - position).length() < 20:
			position = real_dest
		else:
			position += (real_dest - position).normalized() * speed * delta
	else:
		if moving == true:
			arm_left.set_status("idle")
			arm_right.set_status("idle")
		moving = false
	
	if rotation_degrees != rot_dest:
		rotation_degrees += int(rotation_speed * delta * direction)
		
		if rotation_degrees < 0:
			rotation_degrees = 360 + rotation_degrees
		if rotation_degrees >= 360:
			rotation_degrees = rotation_degrees - 360
			
		if abs(rotation_degrees - rot_dest) < 20.0:
			rotation_degrees = rot_dest


func _input(event):
	# react to arrow-keys
	if not moving:
		if event.is_action_pressed("key_up"):
			destination = game.cur_scene.run(destination, Vector2(0, -1))
			set_rot(0)
		elif event.is_action_pressed("key_down"):
			destination = game.cur_scene.run(destination, Vector2(0, 1))
			set_rot(180)
		elif event.is_action_pressed("key_left"):
			destination = game.cur_scene.run(destination, Vector2(-1, 0))
			set_rot(270)
		elif event.is_action_pressed("key_right"):
			destination = game.cur_scene.run(destination, Vector2(1, 0))
			set_rot(90)
		
	
func set_rot(var rot):
	rot_dest = rot
	if int(rotation_degrees + 90) % 360 == rot_dest:
		direction = 1
	else:
		direction = -1
	
