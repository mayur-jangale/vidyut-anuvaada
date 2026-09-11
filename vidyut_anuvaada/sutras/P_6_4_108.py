# Sutra प.6.4.108: नित्यं करोतेः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.108"
SUTRA_TEXT = "नित्यं करोतेः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.108: अग्निः'),
		('रामः', '', 'प.6.4.108: रामः'),
		('सीता', '', 'प.6.4.108: सीता'),
	]

