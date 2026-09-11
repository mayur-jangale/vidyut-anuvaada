# Sutra प.3.1.55: पुषादिद्युताद्यॢदितः परस्मैपदेषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — puzAdidyutAdyxditaH parasmEpadezu

from P_3_1 import apply_3_1_55

SUTRA_CODE = "प.3.1.55"
SUTRA_TEXT = "पुषादिद्युताद्यॢदितः परस्मैपदेषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — puzAdidyutAdyxditaH parasmEpadezu"


class Sutra3155:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.55:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.55:root=रामः;pos='),
		('सीता', '', 'प.3.1.55:root=सीता;pos='),
	]

