# Sutra प.3.4.82: परस्मैपदानां णलतुसुस्थलथुसणल्वमाः
# lṛṭ — simple future endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.82"
SUTRA_TEXT = "परस्मैपदानां णलतुसुस्थलथुसणल्वमाः"
SUTRA_DESC = "lṛṭ — simple future endings"


class Sutra3482:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

