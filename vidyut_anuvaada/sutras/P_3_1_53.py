# Sutra प.3.1.53: लिपिसिचिह्वश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lipisicihvaSca

from P_3_1 import apply_3_1_53

SUTRA_CODE = "प.3.1.53"
SUTRA_TEXT = "लिपिसिचिह्वश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lipisicihvaSca"


class Sutra3153:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.53:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.53:root=रामः;pos='),
		('सीता', '', 'प.3.1.53:root=सीता;pos='),
	]

