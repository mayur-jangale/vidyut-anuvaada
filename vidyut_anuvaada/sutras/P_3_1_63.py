# Sutra प.3.1.63: दुहश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — duhaSca

from P_3_1 import apply_3_1_63

SUTRA_CODE = "प.3.1.63"
SUTRA_TEXT = "दुहश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — duhaSca"


class Sutra3163:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.63:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.63:root=रामः;pos='),
		('सीता', '', 'प.3.1.63:root=सीता;pos='),
	]

