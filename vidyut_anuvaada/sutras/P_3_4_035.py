# Sutra प35: Suzka cUrNa rUkzezu
# Suzka cUrNa rUkzezu pizaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_35

SUTRA_CODE = "प35"
SUTRA_TEXT = "Suzka cUrNa rUkzezu"
SUTRA_DESC = "Suzka cUrNa rUkzezu pizaH"


class Sutra3435:
	def apply(self, word, pos):
		return apply_3_4_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-035:Suzka cUrNa rUkzezu pizaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-035:Suzka cUrNa rUkzezu pizaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-035:Suzka cUrNa rUkzezu pizaH;input=सीता;stem=सीता;ending=-;pos='),
	]

