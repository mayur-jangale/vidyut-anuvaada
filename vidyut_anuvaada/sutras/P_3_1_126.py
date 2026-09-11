# Sutra प.3.1.126: आसुयुवपिरपिलपित्रपिचमश्च
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_126

SUTRA_CODE = "प.3.1.126"
SUTRA_TEXT = "आसुयुवपिरपिलपित्रपिचमश्च"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra31126:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_126(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.126:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.126:root=रामः;pos='),
		('सीता', '', 'प.3.1.126:root=सीता;pos='),
	]

