# Sutra प.3.1.1: प्रत्ययः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pratyayaH

from P_3_1 import apply_3_1_1

SUTRA_CODE = "प.3.1.1"
SUTRA_TEXT = "प्रत्ययः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pratyayaH"


class Sutra311:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.1:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.1:root=रामः;pos='),
		('सीता', '', 'प.3.1.1:root=सीता;pos='),
	]

