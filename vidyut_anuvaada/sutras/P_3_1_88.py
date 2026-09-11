# Sutra प.3.1.88: तपस्तपःकर्मकस्यैव
# vali lopaḥ — elision of व्

from P_3_1 import apply_3_1_88

SUTRA_CODE = "प.3.1.88"
SUTRA_TEXT = "तपस्तपःकर्मकस्यैव"
SUTRA_DESC = "vali lopaḥ — elision of व्"


class Sutra3188:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_88(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.88:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.88:root=रामः;pos='),
		('सीता', '', 'प.3.1.88:root=सीता;pos='),
	]

