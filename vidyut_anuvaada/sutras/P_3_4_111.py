# Sutra प111: laNaH SAkATAyanasyaiva
# laNaH SAkATAyanasyaiva

from sutra_engines import apply_general
from P_3_4 import apply_3_4_111

SUTRA_CODE = "प111"
SUTRA_TEXT = "laNaH SAkATAyanasyaiva"
SUTRA_DESC = "laNaH SAkATAyanasyaiva"


class Sutra34111:
	def apply(self, word, pos):
		return apply_3_4_111(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-111:laNaH SAkATAyanasyaiva;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-111:laNaH SAkATAyanasyaiva;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-111:laNaH SAkATAyanasyaiva;input=सीता;stem=सीता;ending=-;pos='),
	]

