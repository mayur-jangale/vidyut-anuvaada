# Sutra प60: tiryacyapavarge
# tiryacyapavarge

from sutra_engines import apply_general
from P_3_4 import apply_3_4_60

SUTRA_CODE = "प60"
SUTRA_TEXT = "tiryacyapavarge"
SUTRA_DESC = "tiryacyapavarge"


class Sutra3460:
	def apply(self, word, pos):
		return apply_3_4_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-060:tiryacyapavarge;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-060:tiryacyapavarge;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-060:tiryacyapavarge;input=सीता;stem=सीता;ending=-;pos='),
	]

