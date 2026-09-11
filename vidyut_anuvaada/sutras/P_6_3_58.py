# Sutra प.6.3.58: पेषंवासवाहनधिषु च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.58"
SUTRA_TEXT = "पेषंवासवाहनधिषु च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6358:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.58: अग्निः'),
		('रामः', '', 'प.6.3.58: रामः'),
		('सीता', '', 'प.6.3.58: सीता'),
	]

