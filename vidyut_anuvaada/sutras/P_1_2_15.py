# Sutra प.1.2.15: यमो गन्धने
# (Samjna (technical definitions)) — yamo ganDane

from P_1_2 import apply_1_2_15

SUTRA_CODE = "प.1.2.15"
SUTRA_TEXT = "यमो गन्धने"
SUTRA_DESC = "(Samjna (technical definitions)) — yamo ganDane"


class Sutra1215:
	def apply(self, word, pos):
		return apply_1_2_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-yam:अग्निः'),
		('रामः', '', 'non-yam:रामः'),
		('सीता', '', 'non-yam:सीता'),
	]

