# Sutra प.7.2.85: रायो हलि
# (Taddhita (secondary derivations)) — rAyo hali

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.85"
SUTRA_TEXT = "रायो हलि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — rAyo hali"


class Sutra7285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.85: अग्निः'),
		('रामः', '', 'प.7.2.85: रामः'),
		('सीता', '', 'प.7.2.85: सीता'),
	]

