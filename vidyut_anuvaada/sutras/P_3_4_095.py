# Sutra प95: Ata ai
# Ata ai ekAj liG

from sutra_engines import apply_general
from P_3_4 import apply_3_4_95

SUTRA_CODE = "प95"
SUTRA_TEXT = "Ata ai"
SUTRA_DESC = "Ata ai ekAj liG"


class Sutra3495:
	def apply(self, word, pos):
		return apply_3_4_95(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-095:Ata ai ekAj liG;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-095:Ata ai ekAj liG;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-095:Ata ai ekAj liG;input=सीता;stem=सीता;ending=-;pos='),
	]

