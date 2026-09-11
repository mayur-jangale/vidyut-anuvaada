# Sutra प.6.3.23: ऋतो विद्यायोनिसम्बन्धेभ्यः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.23"
SUTRA_TEXT = "ऋतो विद्यायोनिसम्बन्धेभ्यः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6323:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.23: अग्निः'),
		('रामः', '', 'प.6.3.23: रामः'),
		('सीता', '', 'प.6.3.23: सीता'),
	]

