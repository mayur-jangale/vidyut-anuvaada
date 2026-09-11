# Sutra प.6.3.21: षष्ठ्या आक्रोशे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.21"
SUTRA_TEXT = "षष्ठ्या आक्रोशे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.21: अग्निः'),
		('रामः', '', 'प.6.3.21: रामः'),
		('सीता', '', 'प.6.3.21: सीता'),
	]

