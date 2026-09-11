# Sutra प.3.1.111: ई च खनः
# lopo vyorvali — repeated pattern

from P_3_1 import apply_3_1_111

SUTRA_CODE = "प.3.1.111"
SUTRA_TEXT = "ई च खनः"
SUTRA_DESC = "lopo vyorvali — repeated pattern"


class Sutra31111:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_111(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.111:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.111:root=रामः;pos='),
		('सीता', '', 'प.3.1.111:root=सीता;pos='),
	]

