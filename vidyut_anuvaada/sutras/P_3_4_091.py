# Sutra प91: savAByAM vAmO
# savAByAM vAmO

from sutra_engines import apply_general
from P_3_4 import apply_3_4_91

SUTRA_CODE = "प91"
SUTRA_TEXT = "savAByAM vAmO"
SUTRA_DESC = "savAByAM vAmO"


class Sutra3491:
	def apply(self, word, pos):
		return apply_3_4_91(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-091:savAByAM vAmO;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-091:savAByAM vAmO;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-091:savAByAM vAmO;input=सीता;stem=सीता;ending=-;pos='),
	]

