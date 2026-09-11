# Sutra प.7.3.21: देवताद्वन्द्वे च
# (Taddhita (secondary derivations)) — devatAdvandve ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.21"
SUTRA_TEXT = "देवताद्वन्द्वे च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — devatAdvandve ca"


class Sutra7321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.21: अग्निः'),
		('रामः', '', 'प.7.3.21: रामः'),
		('सीता', '', 'प.7.3.21: सीता'),
	]

