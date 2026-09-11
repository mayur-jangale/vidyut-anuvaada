# Sutra प.3.1.67: सार्वधातुके यक्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sArvaDAtuke yak

from P_3_1 import apply_3_1_67

SUTRA_CODE = "प.3.1.67"
SUTRA_TEXT = "सार्वधातुके यक्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sArvaDAtuke yak"


class Sutra3167:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_67(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.67:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.67:root=रामः;pos='),
		('सीता', '', 'प.3.1.67:root=सीता;pos='),
	]

