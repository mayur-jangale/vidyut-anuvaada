# Sutra प.6.3.87: तीर्थे ये
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.87"
SUTRA_TEXT = "तीर्थे ये"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6387:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.87: अग्निः'),
		('रामः', '', 'प.6.3.87: रामः'),
		('सीता', '', 'प.6.3.87: सीता'),
	]

