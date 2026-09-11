# Sutra प.3.1.103: अर्यः स्वामिवैश्ययोः
# lopo vyorvali — repeated pattern

from P_3_1 import apply_3_1_103

SUTRA_CODE = "प.3.1.103"
SUTRA_TEXT = "अर्यः स्वामिवैश्ययोः"
SUTRA_DESC = "lopo vyorvali — repeated pattern"


class Sutra31103:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_103(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.103:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.103:root=रामः;pos='),
		('सीता', '', 'प.3.1.103:root=सीता;pos='),
	]

