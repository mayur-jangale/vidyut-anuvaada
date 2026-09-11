# Sutra प26: svAdumi Ramul
# svAdumi Ramul

from sutra_engines import apply_general
from P_3_4 import apply_3_4_26

SUTRA_CODE = "प26"
SUTRA_TEXT = "svAdumi Ramul"
SUTRA_DESC = "svAdumi Ramul"


class Sutra3426:
	def apply(self, word, pos):
		return apply_3_4_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-026:svAdumi Ramul;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-026:svAdumi Ramul;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-026:svAdumi Ramul;input=सीता;stem=सीता;ending=-;pos='),
	]

