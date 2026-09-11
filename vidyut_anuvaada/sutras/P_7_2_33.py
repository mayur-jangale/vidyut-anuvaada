# Sutra प.7.2.33: सोमे ह्वरितः
# (Taddhita (secondary derivations)) — some hvaritaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.33"
SUTRA_TEXT = "सोमे ह्वरितः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — some hvaritaH"


class Sutra7233:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.33: अग्निः'),
		('रामः', '', 'प.7.2.33: रामः'),
		('सीता', '', 'प.7.2.33: सीता'),
	]

