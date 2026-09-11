# Sutra प.3.1.134: नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_134

SUTRA_CODE = "प.3.1.134"
SUTRA_TEXT = "नन्दिग्रहिपचादिभ्यो ल्युणिन्यचः"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra31134:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_134(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.134:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.134:root=रामः;pos='),
		('सीता', '', 'प.3.1.134:root=सीता;pos='),
	]

