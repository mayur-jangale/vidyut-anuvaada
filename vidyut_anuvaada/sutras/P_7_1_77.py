# Sutra प.7.1.77: ई च द्विवचने
# (Taddhita (secondary derivations)) — I ca dvivacane

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.77"
SUTRA_TEXT = "ई च द्विवचने"
SUTRA_DESC = "(Taddhita (secondary derivations)) — I ca dvivacane"


class Sutra7177:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.77: अग्निः'),
		('रामः', '', 'प.7.1.77: रामः'),
		('सीता', '', 'प.7.1.77: सीता'),
	]

