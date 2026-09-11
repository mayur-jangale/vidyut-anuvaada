# Sutra प52: apAdAne parIpsA
# apAdAne parIpsAyAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_52

SUTRA_CODE = "प52"
SUTRA_TEXT = "apAdAne parIpsA"
SUTRA_DESC = "apAdAne parIpsAyAm"


class Sutra3452:
	def apply(self, word, pos):
		return apply_3_4_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-052:apAdAne parIpsAyAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-052:apAdAne parIpsAyAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-052:apAdAne parIpsAyAm;input=सीता;stem=सीता;ending=-;pos='),
	]

