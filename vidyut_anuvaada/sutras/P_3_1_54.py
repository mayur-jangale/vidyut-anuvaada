# Sutra प.3.1.54: आत्मनेपदेष्वन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtmanepadezvanyatarasyAm

from P_3_1 import apply_3_1_54

SUTRA_CODE = "प.3.1.54"
SUTRA_TEXT = "आत्मनेपदेष्वन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtmanepadezvanyatarasyAm"


class Sutra3154:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.54:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.54:root=रामः;pos='),
		('सीता', '', 'प.3.1.54:root=सीता;pos='),
	]

