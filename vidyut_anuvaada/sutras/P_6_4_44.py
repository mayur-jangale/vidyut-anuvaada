# Sutra प.6.4.44: तनोतेर्यकि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.44"
SUTRA_TEXT = "तनोतेर्यकि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6444:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.44: अग्निः'),
		('रामः', '', 'प.6.4.44: रामः'),
		('सीता', '', 'प.6.4.44: सीता'),
	]

