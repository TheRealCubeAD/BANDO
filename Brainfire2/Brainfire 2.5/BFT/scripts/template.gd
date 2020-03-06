extends Node

var pos
var infected
var connections

var doors

func _init(var x, var y):
	pos = Vector2(x, y)
	infected = false
	doors = [Vector2(0, -1), Vector2(0, 1), Vector2(-1, 0), Vector2(-1, 0)]
	connections = [
		[false, false, false, false],
		[false, false, false, false],
		[false, false, false, false],
		[false, false, false, false]
		]

func equals(var other):
	return pos == other.pos
	
func add_connection(var start, var end):
	connections[doors.find(start)][doors.find(end)]
	
func check(var room):
	for x in range(4):
		for y in range(4):
			if connections[x][y] and not room.connections[x][y]:
				return false
	return true
