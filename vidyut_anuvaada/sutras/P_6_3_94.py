# Sutra प.6.3.94: तिरसस्तिर्यलोपे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.94"
SUTRA_TEXT = "तिरसस्तिर्यलोपे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.94: अग्निः'),
		('रामः', '', 'प.6.3.94: रामः'),
		('सीता', '', 'प.6.3.94: सीता'),
	]

