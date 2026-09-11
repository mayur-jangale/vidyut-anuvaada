# Sutra प101: tasthastha mipAM tAnt
# tasthastha mipAM tAMta tAmaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_101

SUTRA_CODE = "प101"
SUTRA_TEXT = "tasthastha mipAM tAnt"
SUTRA_DESC = "tasthastha mipAM tAMta tAmaH"


class Sutra34101:
	def apply(self, word, pos):
		return apply_3_4_101(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-101:tasthastha mipAM tAMta tAmaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-101:tasthastha mipAM tAMta tAmaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-101:tasthastha mipAM tAMta tAmaH;input=सीता;stem=सीता;ending=-;pos='),
	]

