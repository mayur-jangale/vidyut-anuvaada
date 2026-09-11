# Sutra प.3.1.95: कृत्याः
# lopo vyorvali — repeated pattern

from P_3_1 import apply_3_1_95

SUTRA_CODE = "प.3.1.95"
SUTRA_TEXT = "कृत्याः"
SUTRA_DESC = "lopo vyorvali — repeated pattern"


class Sutra3195:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_95(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.95:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.95:root=रामः;pos='),
		('सीता', '', 'प.3.1.95:root=सीता;pos='),
	]

