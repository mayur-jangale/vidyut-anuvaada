# Sutra प.6.3.26: देवताद्वन्द्वे च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.26"
SUTRA_TEXT = "देवताद्वन्द्वे च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.26: अग्निः'),
		('रामः', '', 'प.6.3.26: रामः'),
		('सीता', '', 'प.6.3.26: सीता'),
	]

