# Sutra प.7.1.96: स्त्रियां च
# (Taddhita (secondary derivations)) — striyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.96"
SUTRA_TEXT = "स्त्रियां च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — striyAM ca"


class Sutra7196:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.96: अग्निः'),
		('रामः', '', 'प.7.1.96: रामः'),
		('सीता', '', 'प.7.1.96: सीता'),
	]

