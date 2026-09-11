# Sutra प.3.1.119: पदास्वैरिबाह्यापक्ष्येषु च
# lopo vyorvali — repeated pattern

from P_3_1 import apply_3_1_119

SUTRA_CODE = "प.3.1.119"
SUTRA_TEXT = "पदास्वैरिबाह्यापक्ष्येषु च"
SUTRA_DESC = "lopo vyorvali — repeated pattern"


class Sutra31119:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_119(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.119:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.119:root=रामः;pos='),
		('सीता', '', 'प.3.1.119:root=सीता;pos='),
	]

