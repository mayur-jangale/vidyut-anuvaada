# Sutra प.7.4.35: न च्छन्दस्यपुत्रस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.35"
SUTRA_TEXT = "न च्छन्दस्यपुत्रस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra7435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.35: अग्निः'),
		('रामः', '', 'प.7.4.35: रामः'),
		('सीता', '', 'प.7.4.35: सीता'),
	]

