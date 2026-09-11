# Sutra प53: dvitIyAyAM ca
# dvitIyAyAM ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_53

SUTRA_CODE = "प53"
SUTRA_TEXT = "dvitIyAyAM ca"
SUTRA_DESC = "dvitIyAyAM ca"


class Sutra3453:
	def apply(self, word, pos):
		return apply_3_4_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-053:dvitIyAyAM ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-053:dvitIyAyAM ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-053:dvitIyAyAM ca;input=सीता;stem=सीता;ending=-;pos='),
	]

