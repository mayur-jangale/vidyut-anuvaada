# Sutra प.6.4.13: सौ च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.13"
SUTRA_TEXT = "सौ च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.13: अग्निः'),
		('रामः', '', 'प.6.4.13: रामः'),
		('सीता', '', 'प.6.4.13: सीता'),
	]

