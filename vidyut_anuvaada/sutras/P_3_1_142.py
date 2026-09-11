# Sutra प.3.1.142: दुन्योरनुपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dunyoranupasarge

from P_3_1 import apply_3_1_142

SUTRA_CODE = "प.3.1.142"
SUTRA_TEXT = "दुन्योरनुपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dunyoranupasarge"


class Sutra31142:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_142(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.142:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.142:root=रामः;pos='),
		('सीता', '', 'प.3.1.142:root=सीता;pos='),
	]

