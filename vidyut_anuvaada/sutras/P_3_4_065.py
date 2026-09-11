# Sutra प65: SakAdi tumun
# Saka tRz etc. arTezu tumun

from sutra_engines import apply_general
from P_3_4 import apply_3_4_65

SUTRA_CODE = "प65"
SUTRA_TEXT = "SakAdi tumun"
SUTRA_DESC = "Saka tRz etc. arTezu tumun"


class Sutra3465:
	def apply(self, word, pos):
		return apply_3_4_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-065:Saka tRz etc. arTezu tumun;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-065:Saka tRz etc. arTezu tumun;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-065:Saka tRz etc. arTezu tumun;input=सीता;stem=सीता;ending=-;pos='),
	]

