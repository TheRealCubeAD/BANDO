extends TileMap


var game

var door_up
var door_down
var door_left
var door_right

var size

var matrix

var binary_tile

func _ready():
	game = get_parent().get_parent().get_parent()
	size = game.room_size
	matrix = get_parent().matrix
	print(matrix)
	
	binary_tile = {
		[0,0,0,0,0]:0,
		[0,0,0,0,1]:29,
		[0,0,0,1,0]:32,
		[0,0,0,1,1]:16,
		[0,0,1,0,0]:30,
		[0,0,1,0,1]:18,
		[0,0,1,1,0]:27,
		[0,0,1,1,1]:22,
		[0,1,0,0,0]:31,
		[0,1,0,0,1]:23,
		[0,1,0,1,0]:17,
		[0,1,0,1,1]:20,
		[0,1,1,0,0]:19,
		[0,1,1,0,1]:26,
		[0,1,1,1,0]:25,
		[0,1,1,1,1]:24,
		[1,0,0,0,0]:-1,
		[1,0,0,0,1]:-1,
		[1,0,0,1,0]:-1,
		[1,0,0,1,1]:2,
		[1,0,1,0,0]:-1,
		[1,0,1,0,1]:1,
		[1,0,1,1,0]:-1,
		[1,0,1,1,1]:5,
		[1,1,0,0,0]:-1,
		[1,1,0,0,1]:-1,
		[1,1,0,1,0]:4,
		[1,1,0,1,1]:10,
		[1,1,1,0,0]:3,
		[1,1,1,0,1]:6,
		[1,1,1,1,0]:8,
		[1,1,1,1,1]:15
	}
	
	# define doors
	door_up = Vector2(size / 2 - 1, -1)
	door_down = Vector2(size / 2, size)
	door_left = Vector2(-1, size / 2 - 1)
	door_right = Vector2(size, size / 2)

	# place edges
	for x in range(-1, size + 1):
		set_cell(x, -1, 28)
		set_cell(x, size, 28)
	for y in range(0, size):
		set_cell(-1, y, 28)
		set_cell(size, y, 28)
	
	#place doors
	for door in [door_down, door_left, door_right, door_up]:
		set_cell(door.x, door.y, -1)
		
	#place walls
	for x in range(size):
		for y in range(size):
			set_cell(x, y, binary_tile[calc_tile(x, y)])
	
func calc_tile(x, y):
	var binary
	
	# if wall on pos
	if matrix[x][y] == 1:
		binary = [
			0,
			calc_tile_get_pos(x - 1, y - 1),
			calc_tile_get_pos(x + 1, y - 1),
			calc_tile_get_pos(x - 1, y + 1),
			calc_tile_get_pos(x + 1, y + 1)
		]
		
		if calc_tile_get_pos(x, y - 1):
			binary[1] = 1
			binary[2] = 1
		if calc_tile_get_pos(x + 1, y):
			binary[2] = 1
			binary[4] = 1
		if calc_tile_get_pos(x, y + 1):
			binary[3] = 1
			binary[4] = 1
		if calc_tile_get_pos(x - 1, y):
			binary[1] = 1
			binary[3] = 1
	
	#if empty on pos
	else:
		binary = [
			1,
			calc_tile_get_pos(x, y - 1),
			calc_tile_get_pos(x - 1, y),
			calc_tile_get_pos(x + 1, y),
			calc_tile_get_pos(x, y + 1)
		]
	
	return binary


func calc_tile_get_pos(x, y):
	if Vector2(x, y) in [door_down, door_left, door_right, door_up]:
		return 0
	if x < 0 or x >= size or y < 0 or y >= size:
		return 1
	else:
		return matrix[x][y]
