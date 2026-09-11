# Sutra प.8.3.7: नश्छव्यप्रशान्
# aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.7"
SUTRA_TEXT = "नश्छव्यप्रशान्"
SUTRA_DESC = "aṅgasya — repeated"


class Sutra837:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.7: अग्निः'),
		('रामः', '', 'प.8.3.7: रामः'),
		('सीता', '', 'प.8.3.7: सीता'),
	]

