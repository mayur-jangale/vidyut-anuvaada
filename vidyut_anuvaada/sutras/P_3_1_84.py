# Sutra प.3.1.84: छन्दसि शायजपि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi SAyajapi

from P_3_1 import apply_3_1_84

SUTRA_CODE = "प.3.1.84"
SUTRA_TEXT = "छन्दसि शायजपि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi SAyajapi"


class Sutra3184:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_84(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.84:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.84:root=रामः;pos='),
		('सीता', '', 'प.3.1.84:root=सीता;pos='),
	]

