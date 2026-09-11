# Sutra प.6.4.16: अज्झनगमां सनि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.16"
SUTRA_TEXT = "अज्झनगमां सनि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.16: अग्निः'),
		('रामः', '', 'प.6.4.16: रामः'),
		('सीता', '', 'प.6.4.16: सीता'),
	]

