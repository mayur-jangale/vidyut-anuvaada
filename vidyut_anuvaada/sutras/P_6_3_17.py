# Sutra प.6.3.17: घकालतनेषु कालनाम्नः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.17"
SUTRA_TEXT = "घकालतनेषु कालनाम्नः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6317:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.17: अग्निः'),
		('रामः', '', 'प.6.3.17: रामः'),
		('सीता', '', 'प.6.3.17: सीता'),
	]

