# Sutra प.8.4.42: न पदान्ताट्टोरनाम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.42"
SUTRA_TEXT = "न पदान्ताट्टोरनाम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8442:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.42: अग्निः'),
		('रामः', '', 'प.8.4.42: रामः'),
		('सीता', '', 'प.8.4.42: सीता'),
	]

