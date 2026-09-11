# Sutra प.7.4.2: नाग्लोपिशास्वृदिताम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.2"
SUTRA_TEXT = "नाग्लोपिशास्वृदिताम्"
SUTRA_DESC = "taddhita — continued"


class Sutra742:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.2: अग्निः'),
		('रामः', '', 'प.7.4.2: रामः'),
		('सीता', '', 'प.7.4.2: सीता'),
	]

