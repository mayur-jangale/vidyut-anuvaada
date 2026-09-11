# Sutra प.1.2.2: विज इट्
# (Samjna (technical definitions)) — vija iw

from P_1_2 import apply_1_2_2

SUTRA_CODE = "प.1.2.2"
SUTRA_TEXT = "विज इट्"
SUTRA_DESC = "(Samjna (technical definitions)) — vija iw"


class Sutra122:
	def apply(self, word, pos):
		return apply_1_2_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-vij:अग्निः'),
		('रामः', '', 'non-vij:रामः'),
		('सीता', '', 'non-vij:सीता'),
	]

