# Sutra प.3.1.52: अस्यतिवक्तिख्यातिभ्योऽङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — asyativaktiKyAtiByo'N

from P_3_1 import apply_3_1_52

SUTRA_CODE = "प.3.1.52"
SUTRA_TEXT = "अस्यतिवक्तिख्यातिभ्योऽङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — asyativaktiKyAtiByo'N"


class Sutra3152:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.52:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.52:root=रामः;pos='),
		('सीता', '', 'प.3.1.52:root=सीता;pos='),
	]

