# Sutra प.3.1.125: ओरावश्यके
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_125

SUTRA_CODE = "प.3.1.125"
SUTRA_TEXT = "ओरावश्यके"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra31125:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_125(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.125:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.125:root=रामः;pos='),
		('सीता', '', 'प.3.1.125:root=सीता;pos='),
	]

