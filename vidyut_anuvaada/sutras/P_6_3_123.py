# Sutra प.6.3.123: इकः काशे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.123"
SUTRA_TEXT = "इकः काशे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.123: अग्निः'),
		('रामः', '', 'प.6.3.123: रामः'),
		('सीता', '', 'प.6.3.123: सीता'),
	]

