# Sutra प.1.4.80: ते प्राग्धातोः
# (Samjna (technical definitions)) — te prAgDAtoH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.80"
SUTRA_TEXT = "ते प्राग्धातोः"
SUTRA_DESC = "(Samjna (technical definitions)) — te prAgDAtoH"


class Sutra1480:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_80
		return apply_1_4_80(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-te-prag:अग्निः'),
		('रामः', '', 'not-te-prag:रामः'),
		('सीता', '', 'not-te-prag:सीता'),
	]

