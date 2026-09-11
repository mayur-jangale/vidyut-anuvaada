# Sutra प.6.3.1: अलुगुत्तरपदे
# final-sandhi — final transformations begin

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.1"
SUTRA_TEXT = "अलुगुत्तरपदे"
SUTRA_DESC = "final-sandhi — final transformations begin"


class Sutra631:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.1: अग्निः'),
		('रामः', '', 'प.6.3.1: रामः'),
		('सीता', '', 'प.6.3.1: सीता'),
	]

