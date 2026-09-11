# Sutra प114: ArDadhAtukaM SezaH
# ArDadhAtukaM SezaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_114

SUTRA_CODE = "प114"
SUTRA_TEXT = "ArDadhAtukaM SezaH"
SUTRA_DESC = "ArDadhAtukaM SezaH"


class Sutra34114:
	def apply(self, word, pos):
		return apply_3_4_114(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-114:ArDadhAtukaM SezaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-114:ArDadhAtukaM SezaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-114:ArDadhAtukaM SezaH;input=सीता;stem=सीता;ending=-;pos='),
	]

