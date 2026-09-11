# Sutra प.7.2.104: कु तिहोः
# (Taddhita (secondary derivations)) — ku tihoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.104"
SUTRA_TEXT = "कु तिहोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ku tihoH"


class Sutra72104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.104: अग्निः'),
		('रामः', '', 'प.7.2.104: रामः'),
		('सीता', '', 'प.7.2.104: सीता'),
	]

