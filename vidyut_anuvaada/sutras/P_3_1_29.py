# Sutra प.3.1.29: ऋतेरीयङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — fterIyaN

from P_3_1 import apply_3_1_29

SUTRA_CODE = "प.3.1.29"
SUTRA_TEXT = "ऋतेरीयङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — fterIyaN"


class Sutra3129:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_29(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.29:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.29:root=रामः;pos='),
		('सीता', '', 'प.3.1.29:root=सीता;pos='),
	]

