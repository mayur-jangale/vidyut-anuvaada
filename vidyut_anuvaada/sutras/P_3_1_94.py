# Sutra प.3.1.94: वाऽसरूपोऽस्त्रियाम्
# vā śnābhyāṃ — repeated pattern

from P_3_1 import apply_3_1_94

SUTRA_CODE = "प.3.1.94"
SUTRA_TEXT = "वाऽसरूपोऽस्त्रियाम्"
SUTRA_DESC = "vā śnābhyāṃ — repeated pattern"


class Sutra3194:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_94(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.94:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.94:root=रामः;pos='),
		('सीता', '', 'प.3.1.94:root=सीता;pos='),
	]

