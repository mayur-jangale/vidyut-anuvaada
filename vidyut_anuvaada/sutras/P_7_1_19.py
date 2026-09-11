# Sutra प.7.1.19: नपुंसकाच्च
# (Taddhita (secondary derivations)) — napuMsakAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.19"
SUTRA_TEXT = "नपुंसकाच्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — napuMsakAcca"


class Sutra7119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.19: अग्निः'),
		('रामः', '', 'प.7.1.19: रामः'),
		('सीता', '', 'प.7.1.19: सीता'),
	]

