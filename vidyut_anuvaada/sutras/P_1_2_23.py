# Sutra प.1.2.23: नोपधात्थफान्ताद्वा
# (Samjna (technical definitions)) — nopaDAtTaPAntAdvA

from P_1_2 import apply_1_2_23

SUTRA_CODE = "प.1.2.23"
SUTRA_TEXT = "नोपधात्थफान्ताद्वा"
SUTRA_DESC = "(Samjna (technical definitions)) — nopaDAtTaPAntAdvA"


class Sutra1223:
	def apply(self, word, pos):
		return apply_1_2_23(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'rule-applies:अग्निः'),
		('रामः', '', 'rule-applies:रामः'),
		('सीता', '', 'rule-applies:सीता'),
	]

