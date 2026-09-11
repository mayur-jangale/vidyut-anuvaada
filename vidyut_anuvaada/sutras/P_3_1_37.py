# Sutra प.3.1.37: दयायासश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dayAyAsaSca

from P_3_1 import apply_3_1_37

SUTRA_CODE = "प.3.1.37"
SUTRA_TEXT = "दयायासश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dayAyAsaSca"


class Sutra3137:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.37:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.37:root=रामः;pos='),
		('सीता', '', 'प.3.1.37:root=सीता;pos='),
	]

