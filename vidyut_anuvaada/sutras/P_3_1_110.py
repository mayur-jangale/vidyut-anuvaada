# Sutra प.3.1.110: ऋदुपधाच्चाकॢपिचृतेः
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_110

SUTRA_CODE = "प.3.1.110"
SUTRA_TEXT = "ऋदुपधाच्चाकॢपिचृतेः"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra31110:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_110(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.110:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.110:root=रामः;pos='),
		('सीता', '', 'प.3.1.110:root=सीता;pos='),
	]

