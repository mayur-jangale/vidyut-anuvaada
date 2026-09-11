# Sutra प.3.1.135: इगुपधज्ञाप्रीकिरः कः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — igupaDajYAprIkiraH kaH

from P_3_1 import apply_3_1_135

SUTRA_CODE = "प.3.1.135"
SUTRA_TEXT = "इगुपधज्ञाप्रीकिरः कः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — igupaDajYAprIkiraH kaH"


class Sutra31135:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_135(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.135:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.135:root=रामः;pos='),
		('सीता', '', 'प.3.1.135:root=सीता;pos='),
	]

