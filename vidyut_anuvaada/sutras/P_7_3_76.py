# Sutra प.7.3.76: क्रमः परस्मैपदेषु
# (Taddhita (secondary derivations)) — kramaH parasmEpadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.76"
SUTRA_TEXT = "क्रमः परस्मैपदेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kramaH parasmEpadezu"


class Sutra7376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.76: अग्निः'),
		('रामः', '', 'प.7.3.76: रामः'),
		('सीता', '', 'प.7.3.76: सीता'),
	]

