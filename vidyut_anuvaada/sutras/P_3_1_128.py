# Sutra प.3.1.128: प्रणाय्योऽसंमतौ
# vali lopaḥ — repeated pattern

from P_3_1 import apply_3_1_128

SUTRA_CODE = "प.3.1.128"
SUTRA_TEXT = "प्रणाय्योऽसंमतौ"
SUTRA_DESC = "vali lopaḥ — repeated pattern"


class Sutra31128:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_128(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.128:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.128:root=रामः;pos='),
		('सीता', '', 'प.3.1.128:root=सीता;pos='),
	]

