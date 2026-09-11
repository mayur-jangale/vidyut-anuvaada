# Sutra प.6.3.61: इको ह्रस्वोऽङ्यो गालवस्य
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.61"
SUTRA_TEXT = "इको ह्रस्वोऽङ्यो गालवस्य"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.61: अग्निः'),
		('रामः', '', 'प.6.3.61: रामः'),
		('सीता', '', 'प.6.3.61: सीता'),
	]

