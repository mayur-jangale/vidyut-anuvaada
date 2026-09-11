# Sutra प.1.4.14: सुप्तिङन्तं पदम्
# sup supā — first sup takes samāsa form when followed by another sup

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.14"
SUTRA_TEXT = "सुप्तिङन्तं पदम्"
SUTRA_DESC = "sup supā — first sup takes samāsa form when followed by another sup"


class Sutra1414:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_14
		return apply_1_4_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-pada:अग्निः'),
		('रामः', '', 'not-pada:रामः'),
		('सीता', '', 'not-pada:सीता'),
	]

