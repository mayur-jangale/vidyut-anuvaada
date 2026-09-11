# Sutra प.6.4.69: न ल्यपि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.69"
SUTRA_TEXT = "न ल्यपि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6469:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.69: अग्निः'),
		('रामः', '', 'प.6.4.69: रामः'),
		('सीता', '', 'प.6.4.69: सीता'),
	]

