# Sutra प.7.2.12: सनि ग्रहगुहोश्च
# (Taddhita (secondary derivations)) — sani grahaguhoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.12"
SUTRA_TEXT = "सनि ग्रहगुहोश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sani grahaguhoSca"


class Sutra7212:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.12: अग्निः'),
		('रामः', '', 'प.7.2.12: रामः'),
		('सीता', '', 'प.7.2.12: सीता'),
	]

