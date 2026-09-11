# Sutra प.3.1.75: अक्षोऽन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — akzo'nyatarasyAm

from P_3_1 import apply_3_1_75

SUTRA_CODE = "प.3.1.75"
SUTRA_TEXT = "अक्षोऽन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — akzo'nyatarasyAm"


class Sutra3175:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_75(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.75:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.75:root=रामः;pos='),
		('सीता', '', 'प.3.1.75:root=सीता;pos='),
	]

