# Sutra प84: BruvaH Adit
# BruvaH paYcAnAm Adit Aho

from sutra_engines import apply_general
from P_3_4 import apply_3_4_84

SUTRA_CODE = "प84"
SUTRA_TEXT = "BruvaH Adit"
SUTRA_DESC = "BruvaH paYcAnAm Adit Aho"


class Sutra3484:
	def apply(self, word, pos):
		return apply_3_4_84(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-084:BruvaH paYcAnAm Adit Aho;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-084:BruvaH paYcAnAm Adit Aho;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-084:BruvaH paYcAnAm Adit Aho;input=सीता;stem=सीता;ending=-;pos='),
	]

