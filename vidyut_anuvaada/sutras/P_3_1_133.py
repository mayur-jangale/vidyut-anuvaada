# Sutra प.3.1.133: ण्वुल्तृचौ
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_133

SUTRA_CODE = "प.3.1.133"
SUTRA_TEXT = "ण्वुल्तृचौ"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra31133:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_133(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.133:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.133:root=रामः;pos='),
		('सीता', '', 'प.3.1.133:root=सीता;pos='),
	]

