# Sutra प.6.3.31: उषासोषसः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.31"
SUTRA_TEXT = "उषासोषसः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.31: अग्निः'),
		('रामः', '', 'प.6.3.31: रामः'),
		('सीता', '', 'प.6.3.31: सीता'),
	]

