# Sutra प.3.1.25: सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — satyApapASarUpavIRAtUlaSlokasenAlomatvacavarmavarRacUrRacurAdiByo Ric

from P_3_1 import apply_3_1_25

SUTRA_CODE = "प.3.1.25"
SUTRA_TEXT = "सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो णिच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — satyApapASarUpavIRAtUlaSlokasenAlomatvacavarmavarRacUrRacurAdiByo Ric"


class Sutra3125:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.25:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.25:root=रामः;pos='),
		('सीता', '', 'प.3.1.25:root=सीता;pos='),
	]

