# Sutra प.7.4.50: तासस्त्योर्लोपः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.50"
SUTRA_TEXT = "तासस्त्योर्लोपः"
SUTRA_DESC = "taddhita — continued"


class Sutra7450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.50: अग्निः'),
		('रामः', '', 'प.7.4.50: रामः'),
		('सीता', '', 'प.7.4.50: सीता'),
	]

