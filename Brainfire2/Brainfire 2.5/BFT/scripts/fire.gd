extends Node2D

func _process(delta):
	# rotation
	get_node("Flame").rotation_degrees += delta * 10
