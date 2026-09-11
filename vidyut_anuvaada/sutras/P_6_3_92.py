# Sutra प.6.3.92: विष्वग्देवयोश्च टेरद्र्यञ्चतावप्रत्यये
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.92"
SUTRA_TEXT = "विष्वग्देवयोश्च टेरद्र्यञ्चतावप्रत्यये"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6392:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.92: अग्निः'),
		('रामः', '', 'प.6.3.92: रामः'),
		('सीता', '', 'प.6.3.92: सीता'),
	]

