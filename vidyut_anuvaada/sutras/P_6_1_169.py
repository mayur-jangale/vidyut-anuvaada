# Sutra प.6.1.169: अन्तोदात्तादुत्तरपदादन्यतरस्यामनित्यसमासे
# sandhi-sūtra प.6.1.169

from P_6_1 import apply_6_1_169

SUTRA_CODE = "प.6.1.169"
SUTRA_TEXT = "अन्तोदात्तादुत्तरपदादन्यतरस्यामनित्यसमासे"
SUTRA_DESC = "sandhi-sūtra प.6.1.169"


class Sutra61169:
	def apply(self, word, pos):
		return apply_6_1_169(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.169:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.169:marker=padartha;input=रामः'),
		('सीता', '', '6.1.169:marker=padartha;input=सीता'),
	]
