# Sutra प.7.3.55: अभ्यासाच्च
# (Taddhita (secondary derivations)) — aByAsAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.55"
SUTRA_TEXT = "अभ्यासाच्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aByAsAcca"


class Sutra7355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.55: अग्निः'),
		('रामः', '', 'प.7.3.55: रामः'),
		('सीता', '', 'प.7.3.55: सीता'),
	]

