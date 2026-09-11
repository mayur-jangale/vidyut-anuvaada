# Sutra प.7.3.117: इदुद्भ्याम्
# (Taddhita (secondary derivations)) — idudByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.117"
SUTRA_TEXT = "इदुद्भ्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — idudByAm"


class Sutra73117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.117: अग्निः'),
		('रामः', '', 'प.7.3.117: रामः'),
		('सीता', '', 'प.7.3.117: सीता'),
	]

