# Sutra प.3.1.2: परश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — paraSca

from P_3_1 import apply_3_1_2

SUTRA_CODE = "प.3.1.2"
SUTRA_TEXT = "परश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — paraSca"


class Sutra312:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.2:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.2:root=रामः;pos='),
		('सीता', '', 'प.3.1.2:root=सीता;pos='),
	]

