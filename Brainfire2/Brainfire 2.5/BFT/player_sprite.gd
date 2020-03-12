extends Sprite

var rot_dest
export var speed = 1000
var direction

func _ready():
	rot_dest = 90
	rotation_degrees = 90
	
func set_rot(var rot):
	rot_dest = rot
	if int(rotation_degrees + 90) % 360 == rot_dest:
		direction = 1
	else:
		direction = -1
	
func _physics_process(delta):
	if rotation_degrees != rot_dest:
		rotation_degrees += int(speed * delta * direction)
		
		if rotation_degrees < 0:
			rotation_degrees = 360 + rotation_degrees
		if rotation_degrees >= 360:
			rotation_degrees = rotation_degrees - 360
			
		if abs(rotation_degrees - rot_dest) < 20.0:
			rotation_degrees = rot_dest
