# Sutra प.3.1.136: आतश्चोपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtaScopasarge

from P_3_1 import apply_3_1_136

SUTRA_CODE = "प.3.1.136"
SUTRA_TEXT = "आतश्चोपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AtaScopasarge"


class Sutra31136:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_136(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.136:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.136:root=रामः;pos='),
		('सीता', '', 'प.3.1.136:root=सीता;pos='),
	]

