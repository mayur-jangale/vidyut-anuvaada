# Sutra प.3.1.57: इरितो वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — irito vA

from P_3_1 import apply_3_1_57

SUTRA_CODE = "प.3.1.57"
SUTRA_TEXT = "इरितो वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — irito vA"


class Sutra3157:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.57:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.57:root=रामः;pos='),
		('सीता', '', 'प.3.1.57:root=सीता;pos='),
	]

