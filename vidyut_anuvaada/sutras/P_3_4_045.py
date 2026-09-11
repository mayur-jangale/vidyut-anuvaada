# Sutra प45: upamAne karmaRi ca
# upamAne karmaRi ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_45

SUTRA_CODE = "प45"
SUTRA_TEXT = "upamAne karmaRi ca"
SUTRA_DESC = "upamAne karmaRi ca"


class Sutra3445:
	def apply(self, word, pos):
		return apply_3_4_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-045:upamAne karmaRi ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-045:upamAne karmaRi ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-045:upamAne karmaRi ca;input=सीता;stem=सीता;ending=-;pos='),
	]

