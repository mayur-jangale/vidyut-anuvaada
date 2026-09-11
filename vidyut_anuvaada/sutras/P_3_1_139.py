# Sutra प.3.1.139: ददातिदधात्योर्विभाषा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dadAtidaDAtyorviBAzA

from P_3_1 import apply_3_1_139

SUTRA_CODE = "प.3.1.139"
SUTRA_TEXT = "ददातिदधात्योर्विभाषा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dadAtidaDAtyorviBAzA"


class Sutra31139:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_139(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.139:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.139:root=रामः;pos='),
		('सीता', '', 'प.3.1.139:root=सीता;pos='),
	]

