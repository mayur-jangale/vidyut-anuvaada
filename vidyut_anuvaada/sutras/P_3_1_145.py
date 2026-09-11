# Sutra प.3.1.145: शिल्पिनि ष्वुन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Silpini zvun

from P_3_1 import apply_3_1_145

SUTRA_CODE = "प.3.1.145"
SUTRA_TEXT = "शिल्पिनि ष्वुन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Silpini zvun"


class Sutra31145:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_145(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.145:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.145:root=रामः;pos='),
		('सीता', '', 'प.3.1.145:root=सीता;pos='),
	]

