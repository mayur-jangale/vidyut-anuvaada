# Sutra प.3.1.38: उषविदजागृभ्योऽन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — uzavidajAgfByo'nyatarasyAm

from P_3_1 import apply_3_1_38

SUTRA_CODE = "प.3.1.38"
SUTRA_TEXT = "उषविदजागृभ्योऽन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — uzavidajAgfByo'nyatarasyAm"


class Sutra3138:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.38:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.38:root=रामः;pos='),
		('सीता', '', 'प.3.1.38:root=सीता;pos='),
	]

