# Sutra प.6.3.55: ऋचः शे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.55"
SUTRA_TEXT = "ऋचः शे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.55: अग्निः'),
		('रामः', '', 'प.6.3.55: रामः'),
		('सीता', '', 'प.6.3.55: सीता'),
	]

