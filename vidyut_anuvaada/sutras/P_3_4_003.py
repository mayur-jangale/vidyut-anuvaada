# Sutra प3: samuccaye-nyatarasyAm
# samuccaye anyatarasyAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_3

SUTRA_CODE = "प3"
SUTRA_TEXT = "samuccaye-nyatarasyAm"
SUTRA_DESC = "samuccaye anyatarasyAm"


class Sutra3403:
	def apply(self, word, pos):
		return apply_3_4_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-003:samuccaye anyatarasyAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-003:samuccaye anyatarasyAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-003:samuccaye anyatarasyAm;input=सीता;stem=सीता;ending=-;pos='),
	]

