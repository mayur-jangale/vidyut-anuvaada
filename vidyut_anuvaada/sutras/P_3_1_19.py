# Sutra प.3.1.19: नमोवरिवश्चित्रङः क्यच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — namovarivaScitraNaH kyac

from P_3_1 import apply_3_1_19

SUTRA_CODE = "प.3.1.19"
SUTRA_TEXT = "नमोवरिवश्चित्रङः क्यच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — namovarivaScitraNaH kyac"


class Sutra3119:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.19:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.19:root=रामः;pos='),
		('सीता', '', 'प.3.1.19:root=सीता;pos='),
	]

