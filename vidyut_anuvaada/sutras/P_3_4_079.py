# Sutra प79: Tit AtmanepadAnAM TeRe
# Tit AtmanepadAnAM TeRe

from sutra_engines import apply_general
from P_3_4 import apply_3_4_79

SUTRA_CODE = "प79"
SUTRA_TEXT = "Tit AtmanepadAnAM TeRe"
SUTRA_DESC = "Tit AtmanepadAnAM TeRe"


class Sutra3479:
	def apply(self, word, pos):
		return apply_3_4_79(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-079:Tit AtmanepadAnAM TeRe;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-079:Tit AtmanepadAnAM TeRe;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-079:Tit AtmanepadAnAM TeRe;input=सीता;stem=सीता;ending=-;pos='),
	]

