# Sutra प39: haste vartti grahoH
# haste vartti grahoH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_39

SUTRA_CODE = "प39"
SUTRA_TEXT = "haste vartti grahoH"
SUTRA_DESC = "haste vartti grahoH"


class Sutra3439:
	def apply(self, word, pos):
		return apply_3_4_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-039:haste vartti grahoH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-039:haste vartti grahoH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-039:haste vartti grahoH;input=सीता;stem=सीता;ending=-;pos='),
	]

