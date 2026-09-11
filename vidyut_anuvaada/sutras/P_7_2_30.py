# Sutra प.7.2.30: अपचितश्च
# (Taddhita (secondary derivations)) — apacitaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.30"
SUTRA_TEXT = "अपचितश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — apacitaSca"


class Sutra7230:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.30: अग्निः'),
		('रामः', '', 'प.7.2.30: रामः'),
		('सीता', '', 'प.7.2.30: सीता'),
	]

