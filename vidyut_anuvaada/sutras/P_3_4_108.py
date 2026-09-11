# Sutra प108: Yer jus
# Yer jus svAsRNAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_108

SUTRA_CODE = "प108"
SUTRA_TEXT = "Yer jus"
SUTRA_DESC = "Yer jus svAsRNAm"


class Sutra34108:
	def apply(self, word, pos):
		return apply_3_4_108(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-108:Yer jus svAsRNAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-108:Yer jus svAsRNAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-108:Yer jus svAsRNAm;input=सीता;stem=सीता;ending=-;pos='),
	]

