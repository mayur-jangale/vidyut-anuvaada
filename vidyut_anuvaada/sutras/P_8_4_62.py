# Sutra प.8.4.62: झयो होऽन्यतरस्याम्
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.62"
SUTRA_TEXT = "झयो होऽन्यतरस्याम्"
SUTRA_DESC = "final transformations — continued"


class Sutra8462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.62: अग्निः'),
		('रामः', '', 'प.8.4.62: रामः'),
		('सीता', '', 'प.8.4.62: सीता'),
	]

