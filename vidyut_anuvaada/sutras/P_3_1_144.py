# Sutra प.3.1.144: गेहे कः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gehe kaH

from P_3_1 import apply_3_1_144

SUTRA_CODE = "प.3.1.144"
SUTRA_TEXT = "गेहे कः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gehe kaH"


class Sutra31144:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_144(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.144:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.144:root=रामः;pos='),
		('सीता', '', 'प.3.1.144:root=सीता;pos='),
	]

