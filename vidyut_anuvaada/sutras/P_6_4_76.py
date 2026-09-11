# Sutra प.6.4.76: इरयो रे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.76"
SUTRA_TEXT = "इरयो रे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.76: अग्निः'),
		('रामः', '', 'प.6.4.76: रामः'),
		('सीता', '', 'प.6.4.76: सीता'),
	]

