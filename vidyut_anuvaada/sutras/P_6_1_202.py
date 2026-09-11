# Sutra प.6.1.202: जयः करणम्
# sandhi-sūtra प.6.1.202

from P_6_1 import apply_6_1_202

SUTRA_CODE = "प.6.1.202"
SUTRA_TEXT = "जयः करणम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.202"


class Sutra61202:
	def apply(self, word, pos):
		return apply_6_1_202(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.202:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.202:marker=padartha;input=रामः'),
		('सीता', '', '6.1.202:marker=padartha;input=सीता'),
	]
