# Sutra प81: liwastaYor eSirec
# liwas taYjor eSirec

from sutra_engines import apply_general
from P_3_4 import apply_3_4_81

SUTRA_CODE = "प81"
SUTRA_TEXT = "liwastaYor eSirec"
SUTRA_DESC = "liwas taYjor eSirec"


class Sutra3481:
	def apply(self, word, pos):
		return apply_3_4_81(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-081:liwas taYjor eSirec;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-081:liwas taYjor eSirec;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-081:liwas taYjor eSirec;input=सीता;stem=सीता;ending=-;pos='),
	]

