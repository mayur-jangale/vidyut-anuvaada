# Sutra प.7.1.80: आच्छीनद्योर्नुम्
# (Taddhita (secondary derivations)) — AcCInadyornum

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.80"
SUTRA_TEXT = "आच्छीनद्योर्नुम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — AcCInadyornum"


class Sutra7180:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.80: अग्निः'),
		('रामः', '', 'प.7.1.80: रामः'),
		('सीता', '', 'प.7.1.80: सीता'),
	]

