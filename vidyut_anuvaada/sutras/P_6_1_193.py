# Sutra प.6.1.193: लिति
# sandhi-sūtra प.6.1.193

from P_6_1 import apply_6_1_193

SUTRA_CODE = "प.6.1.193"
SUTRA_TEXT = "लिति"
SUTRA_DESC = "sandhi-sūtra प.6.1.193"


class Sutra61193:
	def apply(self, word, pos):
		return apply_6_1_193(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.193:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.193:marker=padartha;input=रामः'),
		('सीता', '', '6.1.193:marker=padartha;input=सीता'),
	]
