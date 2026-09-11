# Sutra प.3.1.20: पुच्छभाण्डचीवराण्णिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pucCaBARqacIvarARRiN

from P_3_1 import apply_3_1_20

SUTRA_CODE = "प.3.1.20"
SUTRA_TEXT = "पुच्छभाण्डचीवराण्णिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pucCaBARqacIvarARRiN"


class Sutra3120:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.20:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.20:root=रामः;pos='),
		('सीता', '', 'प.3.1.20:root=सीता;pos='),
	]

