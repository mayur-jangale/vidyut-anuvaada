# Sutra प.7.1.2: आयनेयीनीयियः फढखच्छघां प्रत्ययादीनाम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.2"
SUTRA_TEXT = "आयनेयीनीयियः फढखच्छघां प्रत्ययादीनाम्"
SUTRA_DESC = "taddhita — continued"


class Sutra712:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.2: अग्निः'),
		('रामः', '', 'प.7.1.2: रामः'),
		('सीता', '', 'प.7.1.2: सीता'),
	]

