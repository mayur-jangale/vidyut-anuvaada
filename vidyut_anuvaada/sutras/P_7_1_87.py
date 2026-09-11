# Sutra प.7.1.87: थो न्थः
# (Taddhita (secondary derivations)) — To nTaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.87"
SUTRA_TEXT = "थो न्थः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — To nTaH"


class Sutra7187:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.87: अग्निः'),
		('रामः', '', 'प.7.1.87: रामः'),
		('सीता', '', 'प.7.1.87: सीता'),
	]

