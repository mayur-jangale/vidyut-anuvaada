# Sutra प.7.1.86: इतोऽत् सर्वनामस्थाने
# (Taddhita (secondary derivations)) — ito't sarvanAmasTAne

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.86"
SUTRA_TEXT = "इतोऽत् सर्वनामस्थाने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ito't sarvanAmasTAne"


class Sutra7186:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.86: अग्निः'),
		('रामः', '', 'प.7.1.86: रामः'),
		('सीता', '', 'प.7.1.86: सीता'),
	]

