# Sutra प.7.2.118: किति च
# (Taddhita (secondary derivations)) — kiti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.118"
SUTRA_TEXT = "किति च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kiti ca"


class Sutra72118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.118: अग्निः'),
		('रामः', '', 'प.7.2.118: रामः'),
		('सीता', '', 'प.7.2.118: सीता'),
	]

