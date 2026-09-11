# Sutra प.7.2.98: प्रत्ययोत्तरपदयोश्च
# (Taddhita (secondary derivations)) — pratyayottarapadayoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.98"
SUTRA_TEXT = "प्रत्ययोत्तरपदयोश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — pratyayottarapadayoSca"


class Sutra7298:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.98: अग्निः'),
		('रामः', '', 'प.7.2.98: रामः'),
		('सीता', '', 'प.7.2.98: सीता'),
	]

