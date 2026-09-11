# Sutra प46: kazAdi anuprayogaH
# kazAdizu anuprayogaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_46

SUTRA_CODE = "प46"
SUTRA_TEXT = "kazAdi anuprayogaH"
SUTRA_DESC = "kazAdizu anuprayogaH"


class Sutra3446:
	def apply(self, word, pos):
		return apply_3_4_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-046:kazAdizu anuprayogaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-046:kazAdizu anuprayogaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-046:kazAdizu anuprayogaH;input=सीता;stem=सीता;ending=-;pos='),
	]

