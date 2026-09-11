# Sutra प.6.3.35: तसिलादिष्वाकृत्वसुचः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.35"
SUTRA_TEXT = "तसिलादिष्वाकृत्वसुचः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.35: अग्निः'),
		('रामः', '', 'प.6.3.35: रामः'),
		('सीता', '', 'प.6.3.35: सीता'),
	]

