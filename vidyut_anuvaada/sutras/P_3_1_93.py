# Sutra प.3.1.93: कृदतिङ्
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_93

SUTRA_CODE = "प.3.1.93"
SUTRA_TEXT = "कृदतिङ्"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra3193:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_93(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.93:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.93:root=रामः;pos='),
		('सीता', '', 'प.3.1.93:root=सीता;pos='),
	]

