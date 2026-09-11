# Sutra प.3.1.105: अजर्यं संगतम्
# saṃyogaśiṣṭaḥ — repeated pattern

from P_3_1 import apply_3_1_105

SUTRA_CODE = "प.3.1.105"
SUTRA_TEXT = "अजर्यं संगतम्"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — repeated pattern"


class Sutra31105:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_105(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.105:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.105:root=रामः;pos='),
		('सीता', '', 'प.3.1.105:root=सीता;pos='),
	]

