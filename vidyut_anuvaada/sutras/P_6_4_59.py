# Sutra प.6.4.59: क्षियः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.59"
SUTRA_TEXT = "क्षियः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.59: अग्निः'),
		('रामः', '', 'प.6.4.59: रामः'),
		('सीता', '', 'प.6.4.59: सीता'),
	]

