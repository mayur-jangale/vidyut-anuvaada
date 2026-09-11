# Sutra प.3.1.112: भृञोऽसंज्ञायाम्
# vali lopaḥ — repeated pattern

from P_3_1 import apply_3_1_112

SUTRA_CODE = "प.3.1.112"
SUTRA_TEXT = "भृञोऽसंज्ञायाम्"
SUTRA_DESC = "vali lopaḥ — repeated pattern"


class Sutra31112:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_112(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.112:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.112:root=रामः;pos='),
		('सीता', '', 'प.3.1.112:root=सीता;pos='),
	]

