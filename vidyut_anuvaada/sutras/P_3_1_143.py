# Sutra प.3.1.143: विभाषा ग्रहः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA grahaH

from P_3_1 import apply_3_1_143

SUTRA_CODE = "प.3.1.143"
SUTRA_TEXT = "विभाषा ग्रहः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA grahaH"


class Sutra31143:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_143(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.143:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.143:root=रामः;pos='),
		('सीता', '', 'प.3.1.143:root=सीता;pos='),
	]

