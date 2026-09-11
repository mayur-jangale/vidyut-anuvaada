# Sutra प.3.1.72: संयसश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMyasaSca

from P_3_1 import apply_3_1_72

SUTRA_CODE = "प.3.1.72"
SUTRA_TEXT = "संयसश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMyasaSca"


class Sutra3172:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.72:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.72:root=रामः;pos='),
		('सीता', '', 'प.3.1.72:root=सीता;pos='),
	]

