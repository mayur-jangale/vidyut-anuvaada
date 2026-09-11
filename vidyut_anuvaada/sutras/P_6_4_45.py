# Sutra प.6.4.45: सनः क्तिचि लोपश्चास्यान्यतरस्याम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.45"
SUTRA_TEXT = "सनः क्तिचि लोपश्चास्यान्यतरस्याम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.45: अग्निः'),
		('रामः', '', 'प.6.4.45: रामः'),
		('सीता', '', 'प.6.4.45: सीता'),
	]

