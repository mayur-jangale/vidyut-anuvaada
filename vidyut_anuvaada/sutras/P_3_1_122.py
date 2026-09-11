# Sutra प.3.1.122: अमावस्यदन्यतरस्याम्
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_122

SUTRA_CODE = "प.3.1.122"
SUTRA_TEXT = "अमावस्यदन्यतरस्याम्"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra31122:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_122(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.122:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.122:root=रामः;pos='),
		('सीता', '', 'प.3.1.122:root=सीता;pos='),
	]

