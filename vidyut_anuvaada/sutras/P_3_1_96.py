# Sutra प.3.1.96: तव्यत्तव्यानीयरः
# vali lopaḥ — repeated pattern

from P_3_1 import apply_3_1_96

SUTRA_CODE = "प.3.1.96"
SUTRA_TEXT = "तव्यत्तव्यानीयरः"
SUTRA_DESC = "vali lopaḥ — repeated pattern"


class Sutra3196:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_96(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.96:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.96:root=रामः;pos='),
		('सीता', '', 'प.3.1.96:root=सीता;pos='),
	]

