# Sutra प5: samuccaye sAmAnyavacanasya
# samuccaye sAmAnya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_5

SUTRA_CODE = "प5"
SUTRA_TEXT = "samuccaye sAmAnyavacanasya"
SUTRA_DESC = "samuccaye sAmAnya"


class Sutra3405:
	def apply(self, word, pos):
		return apply_3_4_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-005:samuccaye sAmAnya;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-005:samuccaye sAmAnya;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-005:samuccaye sAmAnya;input=सीता;stem=सीता;ending=-;pos='),
	]

