# Sutra प30: yAvati vindajIvoH
# yAvati vindajIvoH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_30

SUTRA_CODE = "प30"
SUTRA_TEXT = "yAvati vindajIvoH"
SUTRA_DESC = "yAvati vindajIvoH"


class Sutra3430:
	def apply(self, word, pos):
		return apply_3_4_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-030:yAvati vindajIvoH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-030:yAvati vindajIvoH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-030:yAvati vindajIvoH;input=सीता;stem=सीता;ending=-;pos='),
	]

