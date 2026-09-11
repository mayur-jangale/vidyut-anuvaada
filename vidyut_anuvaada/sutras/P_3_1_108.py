# Sutra प.3.1.108: हनस्त च
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_108

SUTRA_CODE = "प.3.1.108"
SUTRA_TEXT = "हनस्त च"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra31108:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_108(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.108:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.108:root=रामः;pos='),
		('सीता', '', 'प.3.1.108:root=सीता;pos='),
	]

