# Sutra प41: aDikaraRe banDaH
# aDikaraRe banDaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_41

SUTRA_CODE = "प41"
SUTRA_TEXT = "aDikaraRe banDaH"
SUTRA_DESC = "aDikaraRe banDaH"


class Sutra3441:
	def apply(self, word, pos):
		return apply_3_4_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-041:aDikaraRe banDaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-041:aDikaraRe banDaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-041:aDikaraRe banDaH;input=सीता;stem=सीता;ending=-;pos='),
	]

