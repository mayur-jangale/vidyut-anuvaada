# Sutra प.3.1.43: च्लि लुङि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — cli luNi

from P_3_1 import apply_3_1_43

SUTRA_CODE = "प.3.1.43"
SUTRA_TEXT = "च्लि लुङि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — cli luNi"


class Sutra3143:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.43:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.43:root=रामः;pos='),
		('सीता', '', 'प.3.1.43:root=सीता;pos='),
	]

