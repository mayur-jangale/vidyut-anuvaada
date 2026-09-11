# Sutra प.3.1.147: ण्युट् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Ryuw ca

from P_3_1 import apply_3_1_147

SUTRA_CODE = "प.3.1.147"
SUTRA_TEXT = "ण्युट् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Ryuw ca"


class Sutra31147:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_147(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.147:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.147:root=रामः;pos='),
		('सीता', '', 'प.3.1.147:root=सीता;pos='),
	]

