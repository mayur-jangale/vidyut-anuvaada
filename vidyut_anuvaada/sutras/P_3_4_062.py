# Sutra प62: na ADA rTa pratyaye
# na ADA'rTa pratyaye cvyarTe

from sutra_engines import apply_general
from P_3_4 import apply_3_4_62

SUTRA_CODE = "प62"
SUTRA_TEXT = "na ADA rTa pratyaye"
SUTRA_DESC = "na ADA'rTa pratyaye cvyarTe"


class Sutra3462:
	def apply(self, word, pos):
		return apply_3_4_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-062:na ADA'rTa pratyaye cvyarTe;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-062:na ADA'rTa pratyaye cvyarTe;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-062:na ADA'rTa pratyaye cvyarTe;input=सीता;stem=सीता;ending=-;pos="),
	]

