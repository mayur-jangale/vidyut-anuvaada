# Sutra प.3.1.50: गुपेश्छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gupeSCandasi

from P_3_1 import apply_3_1_50

SUTRA_CODE = "प.3.1.50"
SUTRA_TEXT = "गुपेश्छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gupeSCandasi"


class Sutra3150:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.50:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.50:root=रामः;pos='),
		('सीता', '', 'प.3.1.50:root=सीता;pos='),
	]

