# Sutra प.6.1.124: इन्द्रे च
# sandhi-sūtra प.6.1.124

from P_6_1 import apply_6_1_124

SUTRA_CODE = "प.6.1.124"
SUTRA_TEXT = "इन्द्रे च"
SUTRA_DESC = "sandhi-sūtra प.6.1.124"


class Sutra61124:
	def apply(self, word, pos):
		return apply_6_1_124(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.124:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.124:marker=padartha;input=रामः'),
		('सीता', '', '6.1.124:marker=padartha;input=सीता'),
	]
