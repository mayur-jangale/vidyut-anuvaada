# Sutra प.7.1.82: सावनडुहः
# (Taddhita (secondary derivations)) — sAvanaquhaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.82"
SUTRA_TEXT = "सावनडुहः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sAvanaquhaH"


class Sutra7182:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.82: अग्निः'),
		('रामः', '', 'प.7.1.82: रामः'),
		('सीता', '', 'प.7.1.82: सीता'),
	]

