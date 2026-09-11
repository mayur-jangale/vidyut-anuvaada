# Sutra प48: hiMsArTa samAna karmaka
# hiMsArTAnAM ca samAnakarmakARAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_48

SUTRA_CODE = "प48"
SUTRA_TEXT = "hiMsArTa samAna karmaka"
SUTRA_DESC = "hiMsArTAnAM ca samAnakarmakARAm"


class Sutra3448:
	def apply(self, word, pos):
		return apply_3_4_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-048:hiMsArTAnAM ca samAnakarmakARAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-048:hiMsArTAnAM ca samAnakarmakARAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-048:hiMsArTAnAM ca samAnakarmakARAm;input=सीता;stem=सीता;ending=-;pos='),
	]

