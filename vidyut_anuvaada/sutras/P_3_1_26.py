# Sutra प.3.1.26: हेतुमति च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — hetumati ca

from P_3_1 import apply_3_1_26

SUTRA_CODE = "प.3.1.26"
SUTRA_TEXT = "हेतुमति च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — hetumati ca"


class Sutra3126:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.26:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.26:root=रामः;pos='),
		('सीता', '', 'प.3.1.26:root=सीता;pos='),
	]

