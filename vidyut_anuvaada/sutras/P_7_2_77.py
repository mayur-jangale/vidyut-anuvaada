# Sutra प.7.2.77: ईशः से
# (Taddhita (secondary derivations)) — ISaH se

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.77"
SUTRA_TEXT = "ईशः से"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ISaH se"


class Sutra7277:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.77: अग्निः'),
		('रामः', '', 'प.7.2.77: रामः'),
		('सीता', '', 'प.7.2.77: सीता'),
	]

