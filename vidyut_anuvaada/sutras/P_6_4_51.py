# Sutra प.6.4.51: णेरनिटि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.51"
SUTRA_TEXT = "णेरनिटि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6451:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.51: अग्निः'),
		('रामः', '', 'प.6.4.51: रामः'),
		('सीता', '', 'प.6.4.51: सीता'),
	]

