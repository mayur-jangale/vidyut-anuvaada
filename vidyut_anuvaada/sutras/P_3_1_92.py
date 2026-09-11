# Sutra प.3.1.92: तत्रोपपदं सप्तमीस्थम्
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_92

SUTRA_CODE = "प.3.1.92"
SUTRA_TEXT = "तत्रोपपदं सप्तमीस्थम्"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra3192:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_92(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.92:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.92:root=रामः;pos='),
		('सीता', '', 'प.3.1.92:root=सीता;pos='),
	]

