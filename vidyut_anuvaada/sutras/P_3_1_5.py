# Sutra प.3.1.5: गुप्तिज्किद्भ्यः सन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — guptijkidByaH san

from P_3_1 import apply_3_1_5

SUTRA_CODE = "प.3.1.5"
SUTRA_TEXT = "गुप्तिज्किद्भ्यः सन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — guptijkidByaH san"


class Sutra315:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.5:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.5:root=रामः;pos='),
		('सीता', '', 'प.3.1.5:root=सीता;pos='),
	]

