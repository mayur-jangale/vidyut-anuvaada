# Sutra प.1.4.56: प्राग्रीश्वरान्निपाताः
# (Samjna (technical definitions)) — prAgrISvarAnnipAtAH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.56"
SUTRA_TEXT = "प्राग्रीश्वरान्निपाताः"
SUTRA_DESC = "(Samjna (technical definitions)) — prAgrISvarAnnipAtAH"


class Sutra1456:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_56
		return apply_1_4_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-prAg:अग्निः'),
		('रामः', '', 'not-prAg:रामः'),
		('सीता', '', 'not-prAg:सीता'),
	]

