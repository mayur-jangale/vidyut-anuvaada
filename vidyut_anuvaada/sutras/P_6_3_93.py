# Sutra प.6.3.93: समः समि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.93"
SUTRA_TEXT = "समः समि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.93: अग्निः'),
		('रामः', '', 'प.6.3.93: रामः'),
		('सीता', '', 'प.6.3.93: सीता'),
	]

