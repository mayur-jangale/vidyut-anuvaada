# Sutra प.7.1.13: ङेर्यः
# (Taddhita (secondary derivations)) — NeryaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.13"
SUTRA_TEXT = "ङेर्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — NeryaH"


class Sutra7113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.13: अग्निः'),
		('रामः', '', 'प.7.1.13: रामः'),
		('सीता', '', 'प.7.1.13: सीता'),
	]

