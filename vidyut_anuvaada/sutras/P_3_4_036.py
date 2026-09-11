# Sutra प36: samUlA hankfY grahaH
# samUlA Akfta jIvezu

from sutra_engines import apply_general
from P_3_4 import apply_3_4_36

SUTRA_CODE = "प36"
SUTRA_TEXT = "samUlA hankfY grahaH"
SUTRA_DESC = "samUlA Akfta jIvezu"


class Sutra3436:
	def apply(self, word, pos):
		return apply_3_4_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-036:samUlA Akfta jIvezu;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-036:samUlA Akfta jIvezu;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-036:samUlA Akfta jIvezu;input=सीता;stem=सीता;ending=-;pos='),
	]

