# Sutra प.7.2.2: अतो ल्रान्तस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.2"
SUTRA_TEXT = "अतो ल्रान्तस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra722:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.2: अग्निः'),
		('रामः', '', 'प.7.2.2: रामः'),
		('सीता', '', 'प.7.2.2: सीता'),
	]

