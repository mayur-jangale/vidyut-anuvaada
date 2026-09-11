# Sutra प.3.1.90: कुषिरजोः प्राचां श्यन् परस्मैपदं च
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_90

SUTRA_CODE = "प.3.1.90"
SUTRA_TEXT = "कुषिरजोः प्राचां श्यन् परस्मैपदं च"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra3190:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_90(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.90:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.90:root=रामः;pos='),
		('सीता', '', 'प.3.1.90:root=सीता;pos='),
	]

