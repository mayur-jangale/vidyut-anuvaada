# Sutra प.7.2.96: तवममौ ङसि
# (Taddhita (secondary derivations)) — tavamamO Nasi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.96"
SUTRA_TEXT = "तवममौ ङसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tavamamO Nasi"


class Sutra7296:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.96: अग्निः'),
		('रामः', '', 'प.7.2.96: रामः'),
		('सीता', '', 'प.7.2.96: सीता'),
	]

