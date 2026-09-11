# Sutra प.6.4.67: एर्लिङि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.67"
SUTRA_TEXT = "एर्लिङि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6467:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.67: अग्निः'),
		('रामः', '', 'प.6.4.67: रामः'),
		('सीता', '', 'प.6.4.67: सीता'),
	]

