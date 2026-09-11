# Sutra प.3.1.22: धातोरेकाचो हलादेः क्रियासमभिहारे यङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtorekAco halAdeH kriyAsamaBihAre yaN

from P_3_1 import apply_3_1_22

SUTRA_CODE = "प.3.1.22"
SUTRA_TEXT = "धातोरेकाचो हलादेः क्रियासमभिहारे यङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtorekAco halAdeH kriyAsamaBihAre yaN"


class Sutra3122:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.22:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.22:root=रामः;pos='),
		('सीता', '', 'प.3.1.22:root=सीता;pos='),
	]

