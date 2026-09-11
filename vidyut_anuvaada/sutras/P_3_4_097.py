# Sutra प97: itaSca lopa parasmEpadeSu
# itaSca lopaH parasmEpadeSu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_97

SUTRA_CODE = "प97"
SUTRA_TEXT = "itaSca lopa parasmEpadeSu"
SUTRA_DESC = "itaSca lopaH parasmEpadeSu"


class Sutra3497:
	def apply(self, word, pos):
		return apply_3_4_97(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-097:itaSca lopaH parasmEpadeSu;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-097:itaSca lopaH parasmEpadeSu;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-097:itaSca lopaH parasmEpadeSu;input=सीता;stem=सीता;ending=-;pos='),
	]

