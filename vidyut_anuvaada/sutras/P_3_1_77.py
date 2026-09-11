# Sutra प.3.1.77: तुदादिभ्यः शः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tudAdiByaH SaH

from P_3_1 import apply_3_1_77

SUTRA_CODE = "प.3.1.77"
SUTRA_TEXT = "तुदादिभ्यः शः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tudAdiByaH SaH"


class Sutra3177:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_77(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.77:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.77:root=रामः;pos='),
		('सीता', '', 'प.3.1.77:root=सीता;pos='),
	]

