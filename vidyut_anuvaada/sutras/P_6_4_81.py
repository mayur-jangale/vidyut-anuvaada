# Sutra प.6.4.81: इणो यण्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.81"
SUTRA_TEXT = "इणो यण्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.81: अग्निः'),
		('रामः', '', 'प.6.4.81: रामः'),
		('सीता', '', 'प.6.4.81: सीता'),
	]

