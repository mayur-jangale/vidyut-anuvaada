# Sutra प.3.1.91: धातोः
# śāṅgyāḥ — repeated pattern

from P_3_1 import apply_3_1_91

SUTRA_CODE = "प.3.1.91"
SUTRA_TEXT = "धातोः"
SUTRA_DESC = "śāṅgyāḥ — repeated pattern"


class Sutra3191:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_91(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.91:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.91:root=रामः;pos='),
		('सीता', '', 'प.3.1.91:root=सीता;pos='),
	]

