extends TileMap

var size
var count_tiles

func _ready():
	size = get_parent().game.room_size / 2 - 1
	count_tiles = 4
	
	# set ice
	for x in range(-1, size + 1):
		for y in range(-1, size + 1):
			var r = randi() % 4
			set_cell(x, y, r)
