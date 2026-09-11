# Sutra प.1.4.85: तृतीयार्थे
# (Samjna (technical definitions)) — tftIyArTe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.85"
SUTRA_TEXT = "तृतीयार्थे"
SUTRA_DESC = "(Samjna (technical definitions)) — tftIyArTe"


class Sutra1485:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_85
		return apply_1_4_85(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-3rd-case:अग्निः'),
		('रामः', '', 'not-3rd-case:रामः'),
		('सीता', '', 'not-3rd-case:सीता'),
	]

