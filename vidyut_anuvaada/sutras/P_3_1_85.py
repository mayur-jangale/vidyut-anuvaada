# Sutra प.3.1.85: व्यत्ययो बहुलम्
# lopo vyorvali — elision of व् before certain suffixes

from P_3_1 import apply_3_1_85

SUTRA_CODE = "प.3.1.85"
SUTRA_TEXT = "व्यत्ययो बहुलम्"
SUTRA_DESC = "lopo vyorvali — elision of व् before certain suffixes"


class Sutra3185:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_85(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.85:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.85:root=रामः;pos='),
		('सीता', '', 'प.3.1.85:root=सीता;pos='),
	]

