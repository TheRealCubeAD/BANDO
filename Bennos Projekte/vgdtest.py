import rawgpy
import json

rawg = rawgpy.RAWG("for_testing:benno.schaab@gmail.com")
res = str(rawg.search("Rainbow Six"))
print(str(rawg.get_game("tom-clancys-rainbow-six-siege-2")))
js = json.loads(res)
pass
pass
pass
