# Sutra प.6.2.52: अनिगन्तोऽञ्चतौ वप्रत्यये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.52"
SUTRA_TEXT = "अनिगन्तोऽञ्चतौ वप्रत्यये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6252:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.52: अग्निः'),
		('रामः', '', 'प.6.2.52: रामः'),
		('सीता', '', 'प.6.2.52: सीता'),
	]

