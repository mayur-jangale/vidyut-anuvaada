# Sutra प.3.1.113: मृजेर्विभाषा
# saṃyogaśiṣṭaḥ — repeated pattern

from P_3_1 import apply_3_1_113

SUTRA_CODE = "प.3.1.113"
SUTRA_TEXT = "मृजेर्विभाषा"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — repeated pattern"


class Sutra31113:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_113(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.113:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.113:root=रामः;pos='),
		('सीता', '', 'प.3.1.113:root=सीता;pos='),
	]

