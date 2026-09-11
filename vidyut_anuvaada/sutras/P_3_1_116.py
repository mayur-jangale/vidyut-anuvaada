# Sutra प.3.1.116: पुष्यसिद्ध्यौ नक्षत्रे
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_116

SUTRA_CODE = "प.3.1.116"
SUTRA_TEXT = "पुष्यसिद्ध्यौ नक्षत्रे"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra31116:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_116(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.116:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.116:root=रामः;pos='),
		('सीता', '', 'प.3.1.116:root=सीता;pos='),
	]

