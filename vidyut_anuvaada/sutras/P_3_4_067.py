# Sutra प67: kartari kft
# kartari kft

from sutra_engines import apply_general
from P_3_4 import apply_3_4_67

SUTRA_CODE = "प67"
SUTRA_TEXT = "kartari kft"
SUTRA_DESC = "kartari kft"


class Sutra3467:
	def apply(self, word, pos):
		return apply_3_4_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-067:kartari kft;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-067:kartari kft;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-067:kartari kft;input=सीता;stem=सीता;ending=-;pos='),
	]

