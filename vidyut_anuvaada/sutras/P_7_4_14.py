# Sutra प.7.4.14: न कपि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.14"
SUTRA_TEXT = "न कपि"
SUTRA_DESC = "taddhita — continued"


class Sutra7414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.14: अग्निः'),
		('रामः', '', 'प.7.4.14: रामः'),
		('सीता', '', 'प.7.4.14: सीता'),
	]

