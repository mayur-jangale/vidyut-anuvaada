# Sutra प4: yaTAviDyanuprayogaH pUrvasmin
# yaTA-vid-anuprayogaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_4

SUTRA_CODE = "प4"
SUTRA_TEXT = "yaTAviDyanuprayogaH pUrvasmin"
SUTRA_DESC = "yaTA-vid-anuprayogaH"


class Sutra3404:
	def apply(self, word, pos):
		return apply_3_4_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-004:yaTA-vid-anuprayogaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-004:yaTA-vid-anuprayogaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-004:yaTA-vid-anuprayogaH;input=सीता;stem=सीता;ending=-;pos='),
	]

