# Sutra प.3.1.24: लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lupasadacarajapajaBadahadaSagFByo BAvagarhAyAm

from P_3_1 import apply_3_1_24

SUTRA_CODE = "प.3.1.24"
SUTRA_TEXT = "लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lupasadacarajapajaBadahadaSagFByo BAvagarhAyAm"


class Sutra3124:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.24:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.24:root=रामः;pos='),
		('सीता', '', 'प.3.1.24:root=सीता;pos='),
	]

