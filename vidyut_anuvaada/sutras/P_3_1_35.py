# Sutra प.3.1.35: कास्प्रत्ययादाममन्त्रे लिटि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAspratyayAdAmamantre liwi

from P_3_1 import apply_3_1_35

SUTRA_CODE = "प.3.1.35"
SUTRA_TEXT = "कास्प्रत्ययादाममन्त्रे लिटि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAspratyayAdAmamantre liwi"


class Sutra3135:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.35:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.35:root=रामः;pos='),
		('सीता', '', 'प.3.1.35:root=सीता;pos='),
	]

