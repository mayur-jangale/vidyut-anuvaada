# Sutra प.3.1.86: लिङ्याशिष्यङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — liNyASizyaN

from P_3_1 import apply_3_1_86

SUTRA_CODE = "प.3.1.86"
SUTRA_TEXT = "लिङ्याशिष्यङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — liNyASizyaN"


class Sutra3186:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_86(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.86:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.86:root=रामः;pos='),
		('सीता', '', 'प.3.1.86:root=सीता;pos='),
	]

