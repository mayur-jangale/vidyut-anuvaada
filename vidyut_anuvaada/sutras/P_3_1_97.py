# Sutra प.3.1.97: अचो यत्
# saṃyogaśiṣṭaḥ — repeated pattern

from P_3_1 import apply_3_1_97

SUTRA_CODE = "प.3.1.97"
SUTRA_TEXT = "अचो यत्"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — repeated pattern"


class Sutra3197:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_97(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.97:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.97:root=रामः;pos='),
		('सीता', '', 'प.3.1.97:root=सीता;pos='),
	]

