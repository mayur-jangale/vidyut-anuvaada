# Sutra प.3.1.98: पोरदुपधात्
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_98

SUTRA_CODE = "प.3.1.98"
SUTRA_TEXT = "पोरदुपधात्"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra3198:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_98(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.98:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.98:root=रामः;pos='),
		('सीता', '', 'प.3.1.98:root=सीता;pos='),
	]

