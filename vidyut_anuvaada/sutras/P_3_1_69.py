# Sutra प.3.1.69: दिवादिभ्यः श्यन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — divAdiByaH Syan

from P_3_1 import apply_3_1_69

SUTRA_CODE = "प.3.1.69"
SUTRA_TEXT = "दिवादिभ्यः श्यन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — divAdiByaH Syan"


class Sutra3169:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.69:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.69:root=रामः;pos='),
		('सीता', '', 'प.3.1.69:root=सीता;pos='),
	]

