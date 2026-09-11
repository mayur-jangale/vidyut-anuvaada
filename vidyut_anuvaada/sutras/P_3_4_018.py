# Sutra प18: alaNKalvoH ktvA
# alaNKalvoH prAcAM ktvA

from sutra_engines import apply_general
from P_3_4 import apply_3_4_18

SUTRA_CODE = "प18"
SUTRA_TEXT = "alaNKalvoH ktvA"
SUTRA_DESC = "alaNKalvoH prAcAM ktvA"


class Sutra3418:
	def apply(self, word, pos):
		return apply_3_4_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-018:alaNKalvoH prAcAM ktvA;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-018:alaNKalvoH prAcAM ktvA;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-018:alaNKalvoH prAcAM ktvA;input=सीता;stem=सीता;ending=-;pos='),
	]

