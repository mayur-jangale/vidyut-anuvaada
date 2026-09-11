# Sutra प.3.1.115: भिद्योद्ध्यौ नदे
# śāṅgyāḥ — repeated pattern

from P_3_1 import apply_3_1_115

SUTRA_CODE = "प.3.1.115"
SUTRA_TEXT = "भिद्योद्ध्यौ नदे"
SUTRA_DESC = "śāṅgyāḥ — repeated pattern"


class Sutra31115:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_115(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.115:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.115:root=रामः;pos='),
		('सीता', '', 'प.3.1.115:root=सीता;pos='),
	]

