extends Node2D

var game
var running_particle
var particle_layer

var matrix

var size
var torch_count

var treshold



func _enter_tree():
	# get values
	game = get_parent().get_parent()
	size = game.room_size
	treshold = game.wall_treshold
	
	running_particle = load("running_particle.tscn")
	particle_layer = get_node("particel_layer")
	
	# calc torch count
	torch_count = size * size / 20
	
	generate_room()


func _ready():
	set_torches()


func generate_room(): # fill matrix randomly
	matrix = []
	for _x in range(size):
		var curr_row = []
		for _y in range(size):
			if randf() < treshold:
				curr_row.append(1)
			else:
				curr_row.append(0)
		matrix.append(curr_row)


func set_torches(): # set torches randomly
	var cur_torch_count = 0
	var torches = []
	var orientations = [Vector2(1,0), Vector2(-1,0), Vector2(0,1), Vector2(0,-1)]
	var layer = get_node("torch_layer")
	
	while cur_torch_count < torch_count:
		print("Torch:",cur_torch_count)
		for _i in range(100):
			var new_torch = Vector2(randi() % size, randi() % size)
			var t
			var help_bool = false
			
			if get_pos_v(new_torch) == 1:
				continue
			for old_torch in torches:
				if (new_torch - old_torch).length() < 6:
					help_bool = true
					break
			if help_bool:
				continue
			for ori in orientations:
				if get_pos_v(new_torch + ori) == 1:
					# set torch
					t = load("res://Fire.tscn").instance()
					t.set_name(str(cur_torch_count))
					layer.add_child(t)
					layer.get_node(str(cur_torch_count)).rotation_degrees = abs(ori.x)*(ori.x + 1) * 90 + (-ori.y) * 90
					layer.get_node(str(cur_torch_count)).position = (new_torch * 200) + Vector2(100, 100)
					torches.append(new_torch)
					print("      Placing:", new_torch, ori, (ori.x + 1) * 90 + (-ori.y) * 90)
					break
			if t != null:
				break
		cur_torch_count += 1


func get_pos_v(vec): # get value in matric from vector
	if vec.x in range(size) and vec.y in range(size):
		return matrix[vec.x][vec.y]
	else:
		return null


func run(pos, dir): # calc pos after running from pos in dir
	var new_pos = pos + dir
	if get_pos_v(new_pos) == 0:
		return run(new_pos, dir)
	else:
		return pos


func summon_particle(pos):
	pos = pos + Vector2(randi() % 100 - 50, randi() % 100 - 50)
	var new = running_particle.instance()
	new.position = pos
	particle_layer.add_child(new)
