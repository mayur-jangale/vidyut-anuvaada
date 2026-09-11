# Sutra प.7.2.26: णेरध्ययने वृत्तम्
# (Taddhita (secondary derivations)) — ReraDyayane vfttam

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.26"
SUTRA_TEXT = "णेरध्ययने वृत्तम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ReraDyayane vfttam"


class Sutra7226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.26: अग्निः'),
		('रामः', '', 'प.7.2.26: रामः'),
		('सीता', '', 'प.7.2.26: सीता'),
	]

