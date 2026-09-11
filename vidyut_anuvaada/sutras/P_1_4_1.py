# Sutra प.1.4.1: आ कडारादेका संज्ञा
# (Samjna (technical definitions)) — A kaqArAdekA saMjYA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.1"
SUTRA_TEXT = "आ कडारादेका संज्ञा"
SUTRA_DESC = "(Samjna (technical definitions)) — A kaqArAdekA saMjYA"


class Sutra141:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_1
		return apply_1_4_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-cluster-samjna:अग्निः'),
		('रामः', '', 'no-cluster-samjna:रामः'),
		('सीता', '', 'no-cluster-samjna:सीता'),
	]

