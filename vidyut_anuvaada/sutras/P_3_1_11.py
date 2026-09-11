# Sutra प.3.1.11: कर्तुः क्यङ् सलोपश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartuH kyaN salopaSca

from P_3_1 import apply_3_1_11

SUTRA_CODE = "प.3.1.11"
SUTRA_TEXT = "कर्तुः क्यङ् सलोपश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartuH kyaN salopaSca"


class Sutra3111:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.11:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.11:root=रामः;pos='),
		('सीता', '', 'प.3.1.11:root=सीता;pos='),
	]

