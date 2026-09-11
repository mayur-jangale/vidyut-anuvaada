# Sutra प.3.1.13: लोहितादिडाज्भ्यः क्यष्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lohitAdiqAjByaH kyaz

from P_3_1 import apply_3_1_13

SUTRA_CODE = "प.3.1.13"
SUTRA_TEXT = "लोहितादिडाज्भ्यः क्यष्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lohitAdiqAjByaH kyaz"


class Sutra3113:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.13:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.13:root=रामः;pos='),
		('सीता', '', 'प.3.1.13:root=सीता;pos='),
	]

