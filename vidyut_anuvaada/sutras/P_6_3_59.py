# Sutra प.6.3.59: एकहलादौ पूरयितव्येऽन्यतरस्याम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.59"
SUTRA_TEXT = "एकहलादौ पूरयितव्येऽन्यतरस्याम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.59: अग्निः'),
		('रामः', '', 'प.6.3.59: रामः'),
		('सीता', '', 'प.6.3.59: सीता'),
	]

