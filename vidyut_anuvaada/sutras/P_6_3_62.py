# Sutra प.6.3.62: एक तद्धिते च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.62"
SUTRA_TEXT = "एक तद्धिते च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6362:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.62: अग्निः'),
		('रामः', '', 'प.6.3.62: रामः'),
		('सीता', '', 'प.6.3.62: सीता'),
	]

