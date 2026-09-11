# Sutra प.3.1.124: ऋहलोर्ण्यत्
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_124

SUTRA_CODE = "प.3.1.124"
SUTRA_TEXT = "ऋहलोर्ण्यत्"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra31124:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_124(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.124:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.124:root=रामः;pos='),
		('सीता', '', 'प.3.1.124:root=सीता;pos='),
	]

