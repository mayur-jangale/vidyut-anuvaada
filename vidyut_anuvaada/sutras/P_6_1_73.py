# Sutra प.6.1.73: छे च
# sandhi-sūtra प.6.1.73

from P_6_1 import apply_6_1_73

SUTRA_CODE = "प.6.1.73"
SUTRA_TEXT = "छे च"
SUTRA_DESC = "sandhi-sūtra प.6.1.73"


class Sutra6173:
	def apply(self, word, pos):
		return apply_6_1_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.73:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.73:marker=padartha;input=रामः'),
		('सीता', '', '6.1.73:marker=padartha;input=सीता'),
	]
