# Sutra प15: avacakze ca
# avacakze ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_15

SUTRA_CODE = "प15"
SUTRA_TEXT = "avacakze ca"
SUTRA_DESC = "avacakze ca"


class Sutra3415:
	def apply(self, word, pos):
		return apply_3_4_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-015:avacakze ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-015:avacakze ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-015:avacakze ca;input=सीता;stem=सीता;ending=-;pos='),
	]

