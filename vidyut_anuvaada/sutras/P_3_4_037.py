# Sutra प37: karaRe hanaH
# karaRe hanaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_37

SUTRA_CODE = "प37"
SUTRA_TEXT = "karaRe hanaH"
SUTRA_DESC = "karaRe hanaH"


class Sutra3437:
	def apply(self, word, pos):
		return apply_3_4_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-037:karaRe hanaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-037:karaRe hanaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-037:karaRe hanaH;input=सीता;stem=सीता;ending=-;pos='),
	]

