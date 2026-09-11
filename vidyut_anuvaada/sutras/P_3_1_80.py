# Sutra प.3.1.80: धिन्विकृण्व्योर च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — DinvikfRvyora ca

from P_3_1 import apply_3_1_80

SUTRA_CODE = "प.3.1.80"
SUTRA_TEXT = "धिन्विकृण्व्योर च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — DinvikfRvyora ca"


class Sutra3180:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_80(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.80:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.80:root=रामः;pos='),
		('सीता', '', 'प.3.1.80:root=सीता;pos='),
	]

