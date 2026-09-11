# Sutra प.7.3.91: गुणोऽपृक्ते
# (Taddhita (secondary derivations)) — guRo'pfkte

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.91"
SUTRA_TEXT = "गुणोऽपृक्ते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — guRo'pfkte"


class Sutra7391:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.91: अग्निः'),
		('रामः', '', 'प.7.3.91: रामः'),
		('सीता', '', 'प.7.3.91: सीता'),
	]

