# Sutra प.8.4.48: नादिन्याक्रोशे पुत्रस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.48"
SUTRA_TEXT = "नादिन्याक्रोशे पुत्रस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8448:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.48: अग्निः'),
		('रामः', '', 'प.8.4.48: रामः'),
		('सीता', '', 'प.8.4.48: सीता'),
	]

