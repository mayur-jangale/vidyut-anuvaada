# Sutra प80: TAsas se
# TAsas se

from sutra_engines import apply_general
from P_3_4 import apply_3_4_80

SUTRA_CODE = "प80"
SUTRA_TEXT = "TAsas se"
SUTRA_DESC = "TAsas se"


class Sutra3480:
	def apply(self, word, pos):
		return apply_3_4_80(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-080:TAsas se;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-080:TAsas se;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-080:TAsas se;input=सीता;stem=सीता;ending=-;pos='),
	]

