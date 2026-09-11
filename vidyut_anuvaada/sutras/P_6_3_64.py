# Sutra प.6.3.64: त्वे च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.64"
SUTRA_TEXT = "त्वे च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.64: अग्निः'),
		('रामः', '', 'प.6.3.64: रामः'),
		('सीता', '', 'प.6.3.64: सीता'),
	]

