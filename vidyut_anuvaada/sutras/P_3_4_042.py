# Sutra प42: saMjYAyAm
# saMjYAyAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_42

SUTRA_CODE = "प42"
SUTRA_TEXT = "saMjYAyAm"
SUTRA_DESC = "saMjYAyAm"


class Sutra3442:
	def apply(self, word, pos):
		return apply_3_4_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-042:saMjYAyAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-042:saMjYAyAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-042:saMjYAyAm;input=सीता;stem=सीता;ending=-;pos='),
	]

