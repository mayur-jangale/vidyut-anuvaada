# Sutra प57: asyati tfza kriyA antare
# asyati tfzaH kriyA'ntare kAlezu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_57

SUTRA_CODE = "प57"
SUTRA_TEXT = "asyati tfza kriyA antare"
SUTRA_DESC = "asyati tfzaH kriyA'ntare kAlezu"


class Sutra3457:
	def apply(self, word, pos):
		return apply_3_4_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-057:asyati tfzaH kriyA'ntare kAlezu;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-057:asyati tfzaH kriyA'ntare kAlezu;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-057:asyati tfzaH kriyA'ntare kAlezu;input=सीता;stem=सीता;ending=-;pos="),
	]

