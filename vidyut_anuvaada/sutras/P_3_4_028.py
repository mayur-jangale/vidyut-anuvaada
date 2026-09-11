# Sutra प28: yaTAtaTA asUyA
# yaTA taTA asUyAprativacane

from sutra_engines import apply_general
from P_3_4 import apply_3_4_28

SUTRA_CODE = "प28"
SUTRA_TEXT = "yaTAtaTA asUyA"
SUTRA_DESC = "yaTA taTA asUyAprativacane"


class Sutra3428:
	def apply(self, word, pos):
		return apply_3_4_28(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-028:yaTA taTA asUyAprativacane;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-028:yaTA taTA asUyAprativacane;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-028:yaTA taTA asUyAprativacane;input=सीता;stem=सीता;ending=-;pos='),
	]

