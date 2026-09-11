# Sutra प.6.3.53: पद् यत्यतदर्थे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.53"
SUTRA_TEXT = "पद् यत्यतदर्थे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6353:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.53: अग्निः'),
		('रामः', '', 'प.6.3.53: रामः'),
		('सीता', '', 'प.6.3.53: सीता'),
	]

