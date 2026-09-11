# Sutra प.8.4.36: नशेः षान्तस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.36"
SUTRA_TEXT = "नशेः षान्तस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.36: अग्निः'),
		('रामः', '', 'प.8.4.36: रामः'),
		('सीता', '', 'प.8.4.36: सीता'),
	]

