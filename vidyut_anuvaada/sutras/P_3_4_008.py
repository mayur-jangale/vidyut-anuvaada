# Sutra प8: upasaMvAdASaNkayoSca
# upasamvAda ASaNka

from sutra_engines import apply_general
from P_3_4 import apply_3_4_8

SUTRA_CODE = "प8"
SUTRA_TEXT = "upasaMvAdASaNkayoSca"
SUTRA_DESC = "upasamvAda ASaNka"


class Sutra3408:
	def apply(self, word, pos):
		return apply_3_4_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-008:upasamvAda ASaNka;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-008:upasamvAda ASaNka;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-008:upasamvAda ASaNka;input=सीता;stem=सीता;ending=-;pos='),
	]

