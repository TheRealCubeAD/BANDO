extends Camera2D

var size_x
var size_y

var c_scale


func _ready():
	# scaling viewport
	c_scale = (get_parent().room_size + 2) * 200.0 / 1080
	zoom = Vector2(c_scale, c_scale)
