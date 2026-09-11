# Sutra प.7.2.60: तासि च कॢपः
# (Taddhita (secondary derivations)) — tAsi ca kxpaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.60"
SUTRA_TEXT = "तासि च कॢपः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tAsi ca kxpaH"


class Sutra7260:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.60: अग्निः'),
		('रामः', '', 'प.7.2.60: रामः'),
		('सीता', '', 'प.7.2.60: सीता'),
	]

