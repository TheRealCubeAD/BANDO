extends Node2D

var game


func _enter_tree():
	game = get_parent()
	position = Vector2((game.room_size + 1) * 200, -200)
	scale = Vector2((game.room_size + 2) * 200.0 / 1080 * 8.4, (game.room_size + 2) * 200.0 / 1080 * 8.4)
	var t = load("Fire.tscn").instance()
	t.position = Vector2(50, 0)

func _ready():
	pass
