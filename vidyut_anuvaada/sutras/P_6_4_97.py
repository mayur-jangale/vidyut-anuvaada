# Sutra प.6.4.97: इस्मन्त्रन्क्विषु च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.97"
SUTRA_TEXT = "इस्मन्त्रन्क्विषु च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6497:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.97: अग्निः'),
		('रामः', '', 'प.6.4.97: रामः'),
		('सीता', '', 'प.6.4.97: सीता'),
	]

