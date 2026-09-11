# Sutra प16: BAvalakzaRe tosun
# BAva-lakzaRe tosun

from sutra_engines import apply_general
from P_3_4 import apply_3_4_16

SUTRA_CODE = "प16"
SUTRA_TEXT = "BAvalakzaRe tosun"
SUTRA_DESC = "BAva-lakzaRe tosun"


class Sutra3416:
	def apply(self, word, pos):
		return apply_3_4_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-016:BAva-lakzaRe tosun;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-016:BAva-lakzaRe tosun;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-016:BAva-lakzaRe tosun;input=सीता;stem=सीता;ending=-;pos='),
	]

