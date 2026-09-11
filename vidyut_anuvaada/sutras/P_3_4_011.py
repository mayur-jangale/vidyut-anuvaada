# Sutra प11: dfSe viKye ca
# dfSe viKye ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_11

SUTRA_CODE = "प11"
SUTRA_TEXT = "dfSe viKye ca"
SUTRA_DESC = "dfSe viKye ca"


class Sutra3411:
	def apply(self, word, pos):
		return apply_3_4_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-011:dfSe viKye ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-011:dfSe viKye ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-011:dfSe viKye ca;input=सीता;stem=सीता;ending=-;pos='),
	]

