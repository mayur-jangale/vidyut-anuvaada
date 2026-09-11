# Sutra प.8.4.38: पदव्यवायेऽपि
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.38"
SUTRA_TEXT = "पदव्यवायेऽपि"
SUTRA_DESC = "final transformations — continued"


class Sutra8438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.38: अग्निः'),
		('रामः', '', 'प.8.4.38: रामः'),
		('सीता', '', 'प.8.4.38: सीता'),
	]

