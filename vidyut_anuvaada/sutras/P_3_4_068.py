# Sutra प68: BavyAdi vA
# Bavya geya etc. vA

from sutra_engines import apply_general
from P_3_4 import apply_3_4_68

SUTRA_CODE = "प68"
SUTRA_TEXT = "BavyAdi vA"
SUTRA_DESC = "Bavya geya etc. vA"


class Sutra3468:
	def apply(self, word, pos):
		return apply_3_4_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-068:Bavya geya etc. vA;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-068:Bavya geya etc. vA;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-068:Bavya geya etc. vA;input=सीता;stem=सीता;ending=-;pos='),
	]

