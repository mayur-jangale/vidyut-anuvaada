# Sutra प.3.1.64: न रुधः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — na ruDaH

from P_3_1 import apply_3_1_64

SUTRA_CODE = "प.3.1.64"
SUTRA_TEXT = "न रुधः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — na ruDaH"


class Sutra3164:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.64:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.64:root=रामः;pos='),
		('सीता', '', 'प.3.1.64:root=सीता;pos='),
	]

