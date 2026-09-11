# Sutra प.6.3.102: रथवदयोश्च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.102"
SUTRA_TEXT = "रथवदयोश्च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.102: अग्निः'),
		('रामः', '', 'प.6.3.102: रामः'),
		('सीता', '', 'प.6.3.102: सीता'),
	]

