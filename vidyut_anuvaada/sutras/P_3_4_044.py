# Sutra प44: UrDve Suzi pUraH
# UrDve Suzi pUraH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_44

SUTRA_CODE = "प44"
SUTRA_TEXT = "UrDve Suzi pUraH"
SUTRA_DESC = "UrDve Suzi pUraH"


class Sutra3444:
	def apply(self, word, pos):
		return apply_3_4_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-044:UrDve Suzi pUraH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-044:UrDve Suzi pUraH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-044:UrDve Suzi pUraH;input=सीता;stem=सीता;ending=-;pos='),
	]

