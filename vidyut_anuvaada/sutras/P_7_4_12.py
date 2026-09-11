# Sutra प.7.4.12: शॄदॄप्रां ह्रस्वो वा
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.12"
SUTRA_TEXT = "शॄदॄप्रां ह्रस्वो वा"
SUTRA_DESC = "taddhita — continued"


class Sutra7412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.12: अग्निः'),
		('रामः', '', 'प.7.4.12: रामः'),
		('सीता', '', 'प.7.4.12: सीता'),
	]

