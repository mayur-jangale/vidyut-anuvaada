# Sutra प51: pramARe ca
# pramARe ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_51

SUTRA_CODE = "प51"
SUTRA_TEXT = "pramARe ca"
SUTRA_DESC = "pramARe ca"


class Sutra3451:
	def apply(self, word, pos):
		return apply_3_4_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-051:pramARe ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-051:pramARe ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-051:pramARe ca;input=सीता;stem=सीता;ending=-;pos='),
	]

