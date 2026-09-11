# Sutra प.7.4.29: गुणोऽर्तिसंयोगाद्योः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.29"
SUTRA_TEXT = "गुणोऽर्तिसंयोगाद्योः"
SUTRA_DESC = "taddhita — continued"


class Sutra7429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.29: अग्निः'),
		('रामः', '', 'प.7.4.29: रामः'),
		('सीता', '', 'प.7.4.29: सीता'),
	]

