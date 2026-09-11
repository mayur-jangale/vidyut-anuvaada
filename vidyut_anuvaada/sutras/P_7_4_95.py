# Sutra प.7.4.95: अत् स्मृदॄत्वरप्रथम्रदस्तॄस्पशाम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.95"
SUTRA_TEXT = "अत् स्मृदॄत्वरप्रथम्रदस्तॄस्पशाम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7495:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.95: अग्निः'),
		('रामः', '', 'प.7.4.95: रामः'),
		('सीता', '', 'प.7.4.95: सीता'),
	]

