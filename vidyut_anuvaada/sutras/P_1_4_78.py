# Sutra प.1.4.78: प्राध्वं बन्धने
# (Samjna (technical definitions)) — prADvaM banDane

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.78"
SUTRA_TEXT = "प्राध्वं बन्धने"
SUTRA_DESC = "(Samjna (technical definitions)) — prADvaM banDane"


class Sutra1478:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_78
		return apply_1_4_78(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-prAGhu:अग्निः'),
		('रामः', '', 'not-prAGhu:रामः'),
		('सीता', '', 'not-prAGhu:सीता'),
	]

