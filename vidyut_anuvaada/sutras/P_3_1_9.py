# Sutra प.3.1.9: काम्यच्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAmyacca

from P_3_1 import apply_3_1_9

SUTRA_CODE = "प.3.1.9"
SUTRA_TEXT = "काम्यच्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAmyacca"


class Sutra319:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.9:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.9:root=रामः;pos='),
		('सीता', '', 'प.3.1.9:root=सीता;pos='),
	]

