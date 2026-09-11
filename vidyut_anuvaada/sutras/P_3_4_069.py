# Sutra प69: laH yat kyap
# laH karmaRi ca BAve cAkarmakeByaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_69

SUTRA_CODE = "प69"
SUTRA_TEXT = "laH yat kyap"
SUTRA_DESC = "laH karmaRi ca BAve cAkarmakeByaH"


class Sutra3469:
	def apply(self, word, pos):
		return apply_3_4_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-069:laH karmaRi ca BAve cAkarmakeByaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-069:laH karmaRi ca BAve cAkarmakeByaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-069:laH karmaRi ca BAve cAkarmakeByaH;input=सीता;stem=सीता;ending=-;pos='),
	]

