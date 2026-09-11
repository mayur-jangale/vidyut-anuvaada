# Sutra प.3.1.121: युग्यं च पत्रे
# saṃyogaśiṣṭaḥ — repeated pattern

from P_3_1 import apply_3_1_121

SUTRA_CODE = "प.3.1.121"
SUTRA_TEXT = "युग्यं च पत्रे"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — repeated pattern"


class Sutra31121:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_121(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.121:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.121:root=रामः;pos='),
		('सीता', '', 'प.3.1.121:root=सीता;pos='),
	]

