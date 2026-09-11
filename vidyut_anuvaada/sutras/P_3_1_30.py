# Sutra प.3.1.30: कमेर्णिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kamerRiN

from P_3_1 import apply_3_1_30

SUTRA_CODE = "प.3.1.30"
SUTRA_TEXT = "कमेर्णिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kamerRiN"


class Sutra3130:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.30:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.30:root=रामः;pos='),
		('सीता', '', 'प.3.1.30:root=सीता;pos='),
	]

