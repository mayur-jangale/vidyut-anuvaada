# Sutra प.3.1.10: उपमानादाचारे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — upamAnAdAcAre

from P_3_1 import apply_3_1_10

SUTRA_CODE = "प.3.1.10"
SUTRA_TEXT = "उपमानादाचारे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — upamAnAdAcAre"


class Sutra3110:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.10:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.10:root=रामः;pos='),
		('सीता', '', 'प.3.1.10:root=सीता;pos='),
	]

