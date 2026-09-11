# Sutra प1: DAtusambanDe pratyayAH
# dhAtu-pratyaya sambandha

from sutra_engines import apply_general
from P_3_4 import apply_3_4_1

SUTRA_CODE = "प1"
SUTRA_TEXT = "DAtusambanDe pratyayAH"
SUTRA_DESC = "dhAtu-pratyaya sambandha"


class Sutra3401:
	def apply(self, word, pos):
		return apply_3_4_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-001:dhAtu-pratyaya sambandha;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-001:dhAtu-pratyaya sambandha;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-001:dhAtu-pratyaya sambandha;input=सीता;stem=सीता;ending=-;pos='),
	]

