# Sutra प.7.1.61: रधिजभोरचि
# (Taddhita (secondary derivations)) — raDijaBoraci

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.61"
SUTRA_TEXT = "रधिजभोरचि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — raDijaBoraci"


class Sutra7161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.61: अग्निः'),
		('रामः', '', 'प.7.1.61: रामः'),
		('सीता', '', 'प.7.1.61: सीता'),
	]

