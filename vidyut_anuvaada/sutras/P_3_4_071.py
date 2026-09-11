# Sutra प71: AdikarmaRi ktaH
# AdikarmaRi ktaH kartari ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_71

SUTRA_CODE = "प71"
SUTRA_TEXT = "AdikarmaRi ktaH"
SUTRA_DESC = "AdikarmaRi ktaH kartari ca"


class Sutra3471:
	def apply(self, word, pos):
		return apply_3_4_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-071:AdikarmaRi ktaH kartari ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-071:AdikarmaRi ktaH kartari ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-071:AdikarmaRi ktaH kartari ca;input=सीता;stem=सीता;ending=-;pos='),
	]

