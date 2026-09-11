# Sutra प72: gatyarTAkarmaka SliSAdi
# gatyarTAkarmaka SliSa SIga

from sutra_engines import apply_general
from P_3_4 import apply_3_4_72

SUTRA_CODE = "प72"
SUTRA_TEXT = "gatyarTAkarmaka SliSAdi"
SUTRA_DESC = "gatyarTAkarmaka SliSa SIga"


class Sutra3472:
	def apply(self, word, pos):
		return apply_3_4_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-072:gatyarTAkarmaka SliSa SIga;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-072:gatyarTAkarmaka SliSa SIga;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-072:gatyarTAkarmaka SliSa SIga;input=सीता;stem=सीता;ending=-;pos='),
	]

