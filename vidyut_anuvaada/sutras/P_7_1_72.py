# Sutra प.7.1.72: नपुंसकस्य झलचः
# (Taddhita (secondary derivations)) — napuMsakasya JalacaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.72"
SUTRA_TEXT = "नपुंसकस्य झलचः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — napuMsakasya JalacaH"


class Sutra7172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.72: अग्निः'),
		('रामः', '', 'प.7.1.72: रामः'),
		('सीता', '', 'प.7.1.72: सीता'),
	]

