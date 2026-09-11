# Sutra प.6.3.137: अन्येषामपि दृश्यते
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.137"
SUTRA_TEXT = "अन्येषामपि दृश्यते"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.137: अग्निः'),
		('रामः', '', 'प.6.3.137: रामः'),
		('सीता', '', 'प.6.3.137: सीता'),
	]

