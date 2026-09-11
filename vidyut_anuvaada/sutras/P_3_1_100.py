# Sutra प.3.1.100: गदमदचरयमश्चानुपसर्गे
# āṭ śānacā — repeated pattern

from P_3_1 import apply_3_1_100

SUTRA_CODE = "प.3.1.100"
SUTRA_TEXT = "गदमदचरयमश्चानुपसर्गे"
SUTRA_DESC = "āṭ śānacā — repeated pattern"


class Sutra31100:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_100(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.100:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.100:root=रामः;pos='),
		('सीता', '', 'प.3.1.100:root=सीता;pos='),
	]

