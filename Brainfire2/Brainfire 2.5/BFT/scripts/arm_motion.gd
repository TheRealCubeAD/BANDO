extends Sprite

export var sin_amplitude = 10
export var sin_speed = 20
var sin_offset = 0

var status = "idle"
var time = 0

func set_status(new_status):
	status = new_status
	time = 0

func _physics_process(delta):
	match status:
		"idle":
			if position.y != -50:
				position.y = int(position.y - min(1, (position.y + 50) / 4))
		
		"running":
			position.y = sin_amplitude * sin(sin_speed * time + sin_offset) - 50
			time += delta
