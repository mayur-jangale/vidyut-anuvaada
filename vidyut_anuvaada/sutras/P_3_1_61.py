# Sutra प.3.1.61: दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dIpajanabuDapUritAyipyAyiByo'nyatarasyAm

from P_3_1 import apply_3_1_61

SUTRA_CODE = "प.3.1.61"
SUTRA_TEXT = "दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dIpajanabuDapUritAyipyAyiByo'nyatarasyAm"


class Sutra3161:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_61(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.61:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.61:root=रामः;pos='),
		('सीता', '', 'प.3.1.61:root=सीता;pos='),
	]

