# Sutra प.1.4.26: पराजेरसोढः
# (Samjna (technical definitions)) — parAjerasoQaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.26"
SUTRA_TEXT = "पराजेरसोढः"
SUTRA_DESC = "(Samjna (technical definitions)) — parAjerasoQaH"


class Sutra1426:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_26
		return apply_1_4_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-parAjita:अग्निः'),
		('रामः', '', 'not-parAjita:रामः'),
		('सीता', '', 'not-parAjita:सीता'),
	]

