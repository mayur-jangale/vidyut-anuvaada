# Sutra प.7.4.11: ऋच्छत्यॄताम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.11"
SUTRA_TEXT = "ऋच्छत्यॄताम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.11: अग्निः'),
		('रामः', '', 'प.7.4.11: रामः'),
		('सीता', '', 'प.7.4.11: सीता'),
	]

