# Sutra प66: paryApti tavya anIya
# paryApte vacanezu alaM arTezu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_66

SUTRA_CODE = "प66"
SUTRA_TEXT = "paryApti tavya anIya"
SUTRA_DESC = "paryApte vacanezu alaM arTezu"


class Sutra3466:
	def apply(self, word, pos):
		return apply_3_4_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-066:paryApte vacanezu alaM arTezu;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-066:paryApte vacanezu alaM arTezu;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-066:paryApte vacanezu alaM arTezu;input=सीता;stem=सीता;ending=-;pos='),
	]

