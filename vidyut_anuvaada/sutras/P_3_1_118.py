# Sutra प.3.1.118: प्रत्यपिभ्यां ग्रहेश्छन्दसि
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_118

SUTRA_CODE = "प.3.1.118"
SUTRA_TEXT = "प्रत्यपिभ्यां ग्रहेश्छन्दसि"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra31118:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_118(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.118:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.118:root=रामः;pos='),
		('सीता', '', 'प.3.1.118:root=सीता;pos='),
	]

