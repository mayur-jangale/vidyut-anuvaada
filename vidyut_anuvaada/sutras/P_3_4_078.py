# Sutra प78: tiN pratyaya
# tiptas-jhi-sip-thas-mip-vas-mas

from sutra_engines import apply_general
from P_3_4 import apply_3_4_78

SUTRA_CODE = "प78"
SUTRA_TEXT = "tiN pratyaya"
SUTRA_DESC = "tiptas-jhi-sip-thas-mip-vas-mas"


class Sutra3478:
	def apply(self, word, pos):
		return apply_3_4_78(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-078:tiptas-jhi-sip-thas-mip-vas-mas;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-078:tiptas-jhi-sip-thas-mip-vas-mas;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-078:tiptas-jhi-sip-thas-mip-vas-mas;input=सीता;stem=सीता;ending=-;pos='),
	]

