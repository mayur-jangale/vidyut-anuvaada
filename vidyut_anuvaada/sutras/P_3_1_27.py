# Sutra प.3.1.27: कण्ड्वादिभ्यो यक्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kaRqvAdiByo yak

from P_3_1 import apply_3_1_27

SUTRA_CODE = "प.3.1.27"
SUTRA_TEXT = "कण्ड्वादिभ्यो यक्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kaRqvAdiByo yak"


class Sutra3127:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_27(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.27:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.27:root=रामः;pos='),
		('सीता', '', 'प.3.1.27:root=सीता;pos='),
	]

