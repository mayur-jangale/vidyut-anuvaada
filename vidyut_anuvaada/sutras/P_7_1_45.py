# Sutra प.7.1.45: तप्तनप्तनथनाश्च
# (Taddhita (secondary derivations)) — taptanaptanaTanASca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.45"
SUTRA_TEXT = "तप्तनप्तनथनाश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — taptanaptanaTanASca"


class Sutra7145:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.45: अग्निः'),
		('रामः', '', 'प.7.1.45: रामः'),
		('सीता', '', 'प.7.1.45: सीता'),
	]

