# Sutra प.3.1.8: सुप आत्मनः क्यच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — supa AtmanaH kyac

from P_3_1 import apply_3_1_8

SUTRA_CODE = "प.3.1.8"
SUTRA_TEXT = "सुप आत्मनः क्यच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — supa AtmanaH kyac"


class Sutra318:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.8:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.8:root=रामः;pos='),
		('सीता', '', 'प.3.1.8:root=सीता;pos='),
	]

