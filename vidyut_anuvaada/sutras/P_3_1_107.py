# Sutra प.3.1.107: भुवो भावे
# śāṅgyāḥ — repeated pattern

from P_3_1 import apply_3_1_107

SUTRA_CODE = "प.3.1.107"
SUTRA_TEXT = "भुवो भावे"
SUTRA_DESC = "śāṅgyāḥ — repeated pattern"


class Sutra31107:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_107(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.107:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.107:root=रामः;pos='),
		('सीता', '', 'प.3.1.107:root=सीता;pos='),
	]

