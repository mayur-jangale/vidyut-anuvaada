# Sutra प.7.1.71: युजेरसमासे
# (Taddhita (secondary derivations)) — yujerasamAse

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.71"
SUTRA_TEXT = "युजेरसमासे"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yujerasamAse"


class Sutra7171:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.71: अग्निः'),
		('रामः', '', 'प.7.1.71: रामः'),
		('सीता', '', 'प.7.1.71: सीता'),
	]

