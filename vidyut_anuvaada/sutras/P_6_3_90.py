# Sutra प.6.3.90: इदङ्किमोरीश्की
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.90"
SUTRA_TEXT = "इदङ्किमोरीश्की"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6390:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.90: अग्निः'),
		('रामः', '', 'प.6.3.90: रामः'),
		('सीता', '', 'प.6.3.90: सीता'),
	]

