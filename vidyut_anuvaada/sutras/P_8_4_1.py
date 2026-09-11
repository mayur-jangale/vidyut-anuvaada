# Sutra प.8.4.1: रषाभ्यां नो णः समानपदे
# final transformations — final sandhi and replacement rules

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.1"
SUTRA_TEXT = "रषाभ्यां नो णः समानपदे"
SUTRA_DESC = "final transformations — final sandhi and replacement rules"


class Sutra841:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.1: अग्निः'),
		('रामः', '', 'प.8.4.1: रामः'),
		('सीता', '', 'प.8.4.1: सीता'),
	]

