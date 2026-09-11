# Sutra प70: tayoH gaw
# tayoH eva kftya-kta-Kal-arthaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_70

SUTRA_CODE = "प70"
SUTRA_TEXT = "tayoH gaw"
SUTRA_DESC = "tayoH eva kftya-kta-Kal-arthaH"


class Sutra3470:
	def apply(self, word, pos):
		return apply_3_4_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-070:tayoH eva kftya-kta-Kal-arthaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-070:tayoH eva kftya-kta-Kal-arthaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-070:tayoH eva kftya-kta-Kal-arthaH;input=सीता;stem=सीता;ending=-;pos='),
	]

