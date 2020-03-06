extends Node

var size
var rooms
var templates
var start_pos
var end_pos
var path

var room_object = load("res://scripts/room.gd")
var template_object = load("res://scripts/template.gd")



func _init(var level_size):
	size = level_size
	
	#init room matrix
	rooms = []
	for _x in range(size):
		var row = []
		for _y in range(size):
			row.append(null)
		rooms.append(row)
	
	#init template matrix
	templates = []
	for x in range(size):
		var row = []
		for y in range(size):
			row.append(template_object.new(x, y))
		templates.append(row)
	
func create_tpl_matrix():
	# init not_infected
	var not_infected = []
	for row in templates:
		not_infected += row
	not_infected.erase(templates[start_pos.x][start_pos.y])
	
	templates[start_pos.x][start_pos.y].infected = true
	#TBC
	
