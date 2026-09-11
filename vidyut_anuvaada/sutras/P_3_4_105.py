# Sutra प105: Yasya ran
# Yasya ran

from sutra_engines import apply_general
from P_3_4 import apply_3_4_105

SUTRA_CODE = "प105"
SUTRA_TEXT = "Yasya ran"
SUTRA_DESC = "Yasya ran"


class Sutra34105:
	def apply(self, word, pos):
		return apply_3_4_105(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-105:Yasya ran;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-105:Yasya ran;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-105:Yasya ran;input=सीता;stem=सीता;ending=-;pos='),
	]

