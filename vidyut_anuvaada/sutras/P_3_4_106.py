# Sutra प106: iTo at
# iTo at Snasor

from sutra_engines import apply_general
from P_3_4 import apply_3_4_106

SUTRA_CODE = "प106"
SUTRA_TEXT = "iTo at"
SUTRA_DESC = "iTo at Snasor"


class Sutra34106:
	def apply(self, word, pos):
		return apply_3_4_106(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-106:iTo at Snasor;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-106:iTo at Snasor;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-106:iTo at Snasor;input=सीता;stem=सीता;ending=-;pos='),
	]

