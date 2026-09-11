# Sutra प.6.2.87: प्रस्थेऽवृद्धमकर्क्यादीनाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.87"
SUTRA_TEXT = "प्रस्थेऽवृद्धमकर्क्यादीनाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6287:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.87: अग्निः'),
		('रामः', '', 'प.6.2.87: रामः'),
		('सीता', '', 'प.6.2.87: सीता'),
	]

