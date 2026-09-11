# Sutra प13: ISvare tosunkasunO
# ISvare tosun kasunO

from sutra_engines import apply_general
from P_3_4 import apply_3_4_13

SUTRA_CODE = "प13"
SUTRA_TEXT = "ISvare tosunkasunO"
SUTRA_DESC = "ISvare tosun kasunO"


class Sutra3413:
	def apply(self, word, pos):
		return apply_3_4_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-013:ISvare tosun kasunO;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-013:ISvare tosun kasunO;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-013:ISvare tosun kasunO;input=सीता;stem=सीता;ending=-;pos='),
	]

