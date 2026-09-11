# Sutra प21: lyap
# samAna-kartfkoH pUrvakAle lyap

from sutra_engines import apply_general
from P_3_4 import apply_3_4_21

SUTRA_CODE = "प21"
SUTRA_TEXT = "lyap"
SUTRA_DESC = "samAna-kartfkoH pUrvakAle lyap"


class Sutra3421:
	def apply(self, word, pos):
		return apply_3_4_21(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-021:samAna-kartfkoH pUrvakAle lyap;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-021:samAna-kartfkoH pUrvakAle lyap;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-021:samAna-kartfkoH pUrvakAle lyap;input=सीता;stem=सीता;ending=-;pos='),
	]

