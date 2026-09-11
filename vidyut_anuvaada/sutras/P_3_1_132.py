# Sutra प.3.1.132: चित्याग्निचित्ये च
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_132

SUTRA_CODE = "प.3.1.132"
SUTRA_TEXT = "चित्याग्निचित्ये च"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra31132:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_132(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.132:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.132:root=रामः;pos='),
		('सीता', '', 'प.3.1.132:root=सीता;pos='),
	]

