# Sutra प56: viSi pati padi skanda
# viSi pati padi skandAM vyApya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_56

SUTRA_CODE = "प56"
SUTRA_TEXT = "viSi pati padi skanda"
SUTRA_DESC = "viSi pati padi skandAM vyApya"


class Sutra3456:
	def apply(self, word, pos):
		return apply_3_4_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-056:viSi pati padi skandAM vyApya;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-056:viSi pati padi skandAM vyApya;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-056:viSi pati padi skandAM vyApya;input=सीता;stem=सीता;ending=-;pos='),
	]

