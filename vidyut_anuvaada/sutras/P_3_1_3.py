# Sutra प.3.1.3: आद्युदात्तश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AdyudAttaSca

from P_3_1 import apply_3_1_3

SUTRA_CODE = "प.3.1.3"
SUTRA_TEXT = "आद्युदात्तश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AdyudAttaSca"


class Sutra313:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.3:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.3:root=रामः;pos='),
		('सीता', '', 'प.3.1.3:root=सीता;pos='),
	]

