# Sutra प.3.1.99: शकिसहोश्च
# śāṅgyāḥ — repeated pattern

from P_3_1 import apply_3_1_99

SUTRA_CODE = "प.3.1.99"
SUTRA_TEXT = "शकिसहोश्च"
SUTRA_DESC = "śāṅgyāḥ — repeated pattern"


class Sutra3199:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_99(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.99:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.99:root=रामः;pos='),
		('सीता', '', 'प.3.1.99:root=सीता;pos='),
	]

