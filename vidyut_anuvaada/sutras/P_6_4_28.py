# Sutra प.6.4.28: स्यदो जवे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.28"
SUTRA_TEXT = "स्यदो जवे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.28: अग्निः'),
		('रामः', '', 'प.6.4.28: रामः'),
		('सीता', '', 'प.6.4.28: सीता'),
	]

