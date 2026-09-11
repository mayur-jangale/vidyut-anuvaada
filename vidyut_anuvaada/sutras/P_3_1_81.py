# Sutra प.3.1.81: क्र्यादिभ्यः श्ना
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kryAdiByaH SnA

from P_3_1 import apply_3_1_81

SUTRA_CODE = "प.3.1.81"
SUTRA_TEXT = "क्र्यादिभ्यः श्ना"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kryAdiByaH SnA"


class Sutra3181:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_81(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.81:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.81:root=रामः;pos='),
		('सीता', '', 'प.3.1.81:root=सीता;pos='),
	]

