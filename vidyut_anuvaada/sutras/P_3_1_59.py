# Sutra प.3.1.59: कृमृदृरुहिभ्यश्छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfmfdfruhiByaSCandasi

from P_3_1 import apply_3_1_59

SUTRA_CODE = "प.3.1.59"
SUTRA_TEXT = "कृमृदृरुहिभ्यश्छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfmfdfruhiByaSCandasi"


class Sutra3159:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.59:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.59:root=रामः;pos='),
		('सीता', '', 'प.3.1.59:root=सीता;pos='),
	]

