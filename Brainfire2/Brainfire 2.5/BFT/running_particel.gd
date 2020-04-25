extends Sprite

func _process(delta):
	scale -= Vector2(1/(scale.length() * 5), 1/(scale.length() * 5))
	if scale.x <= 0:
		free()
