# Sutra प.7.3.60: अजिव्रज्योश्च
# (Taddhita (secondary derivations)) — ajivrajyoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.60"
SUTRA_TEXT = "अजिव्रज्योश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ajivrajyoSca"


class Sutra7360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.60: अग्निः'),
		('रामः', '', 'प.7.3.60: रामः'),
		('सीता', '', 'प.7.3.60: सीता'),
	]

