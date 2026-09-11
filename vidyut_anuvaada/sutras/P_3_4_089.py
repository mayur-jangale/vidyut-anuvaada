# Sutra प89: mer niH
# mer niH lRG

from sutra_engines import apply_general
from P_3_4 import apply_3_4_89

SUTRA_CODE = "प89"
SUTRA_TEXT = "mer niH"
SUTRA_DESC = "mer niH lRG"


class Sutra3489:
	def apply(self, word, pos):
		return apply_3_4_89(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-089:mer niH lRG;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-089:mer niH lRG;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-089:mer niH lRG;input=सीता;stem=सीता;ending=-;pos='),
	]

