# Sutra प.7.1.90: गोतो णित्
# (Taddhita (secondary derivations)) — goto Rit

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.90"
SUTRA_TEXT = "गोतो णित्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — goto Rit"


class Sutra7190:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.90: अग्निः'),
		('रामः', '', 'प.7.1.90: रामः'),
		('सीता', '', 'प.7.1.90: सीता'),
	]

