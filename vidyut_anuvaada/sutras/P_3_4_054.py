# Sutra प54: svANge aDruve
# svANge aDruve

from sutra_engines import apply_general
from P_3_4 import apply_3_4_54

SUTRA_CODE = "प54"
SUTRA_TEXT = "svANge aDruve"
SUTRA_DESC = "svANge aDruve"


class Sutra3454:
	def apply(self, word, pos):
		return apply_3_4_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-054:svANge aDruve;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-054:svANge aDruve;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-054:svANge aDruve;input=सीता;stem=सीता;ending=-;pos='),
	]

