# Sutra प.3.1.40: कृञ् चानुप्रयुज्यते लिटि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfY cAnuprayujyate liwi

from P_3_1 import apply_3_1_40

SUTRA_CODE = "प.3.1.40"
SUTRA_TEXT = "कृञ् चानुप्रयुज्यते लिटि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfY cAnuprayujyate liwi"


class Sutra3140:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.40:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.40:root=रामः;pos='),
		('सीता', '', 'प.3.1.40:root=सीता;pos='),
	]

