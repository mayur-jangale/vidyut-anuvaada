# Sutra प.6.4.89: ऊदुपधाया गोहः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.89"
SUTRA_TEXT = "ऊदुपधाया गोहः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6489:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.89: अग्निः'),
		('रामः', '', 'प.6.4.89: रामः'),
		('सीता', '', 'प.6.4.89: सीता'),
	]

