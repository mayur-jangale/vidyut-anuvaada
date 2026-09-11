# Sutra प.3.1.31: आयादय आर्धद्धातुके वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AyAdaya ArDadDAtuke vA

from P_3_1 import apply_3_1_31

SUTRA_CODE = "प.3.1.31"
SUTRA_TEXT = "आयादय आर्धद्धातुके वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AyAdaya ArDadDAtuke vA"


class Sutra3131:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.31:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.31:root=रामः;pos='),
		('सीता', '', 'प.3.1.31:root=सीता;pos='),
	]

