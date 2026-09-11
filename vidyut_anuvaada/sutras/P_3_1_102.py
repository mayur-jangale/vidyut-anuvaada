# Sutra प.3.1.102: वह्यं करणम्
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_102

SUTRA_CODE = "प.3.1.102"
SUTRA_TEXT = "वह्यं करणम्"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra31102:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_102(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.102:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.102:root=रामः;pos='),
		('सीता', '', 'प.3.1.102:root=सीता;pos='),
	]

