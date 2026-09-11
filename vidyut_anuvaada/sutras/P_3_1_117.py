# Sutra प.3.1.117: विपूयविनीयजित्या मुञ्जकल्कहलिषु
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_117

SUTRA_CODE = "प.3.1.117"
SUTRA_TEXT = "विपूयविनीयजित्या मुञ्जकल्कहलिषु"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra31117:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_117(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.117:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.117:root=रामः;pos='),
		('सीता', '', 'प.3.1.117:root=सीता;pos='),
	]

