# Sutra प55: parikliSyamAne ca
# parikliSyamAne ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_55

SUTRA_CODE = "प55"
SUTRA_TEXT = "parikliSyamAne ca"
SUTRA_DESC = "parikliSyamAne ca"


class Sutra3455:
	def apply(self, word, pos):
		return apply_3_4_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-055:parikliSyamAne ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-055:parikliSyamAne ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-055:parikliSyamAne ca;input=सीता;stem=सीता;ending=-;pos='),
	]

