# Sutra प.7.3.105: आङि चापः
# (Taddhita (secondary derivations)) — ANi cApaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.105"
SUTRA_TEXT = "आङि चापः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ANi cApaH"


class Sutra73105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.105: अग्निः'),
		('रामः', '', 'प.7.3.105: रामः'),
		('सीता', '', 'प.7.3.105: सीता'),
	]

