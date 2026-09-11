# Sutra प.6.3.15: प्रावृट्शरत्कालदिवां जे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.15"
SUTRA_TEXT = "प्रावृट्शरत्कालदिवां जे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.15: अग्निः'),
		('रामः', '', 'प.6.3.15: रामः'),
		('सीता', '', 'प.6.3.15: सीता'),
	]

