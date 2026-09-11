# Sutra प.6.4.118: लोपो यि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.118"
SUTRA_TEXT = "लोपो यि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.118: अग्निः'),
		('रामः', '', 'प.6.4.118: रामः'),
		('सीता', '', 'प.6.4.118: सीता'),
	]

