# Sutra प.3.1.150: आशिषि च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASizi ca

from P_3_1 import apply_3_1_150

SUTRA_CODE = "प.3.1.150"
SUTRA_TEXT = "आशिषि च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASizi ca"


class Sutra31150:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_150(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.150:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.150:root=रामः;pos='),
		('सीता', '', 'प.3.1.150:root=सीता;pos='),
	]

