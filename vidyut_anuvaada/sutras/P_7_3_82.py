# Sutra प.7.3.82: मिदेर्गुणः
# (Taddhita (secondary derivations)) — miderguRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.82"
SUTRA_TEXT = "मिदेर्गुणः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — miderguRaH"


class Sutra7382:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.82: अग्निः'),
		('रामः', '', 'प.7.3.82: रामः'),
		('सीता', '', 'प.7.3.82: सीता'),
	]

