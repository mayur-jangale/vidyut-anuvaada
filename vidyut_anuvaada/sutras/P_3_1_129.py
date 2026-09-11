# Sutra प.3.1.129: पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु
# saṃyogaśiṣṭaḥ — repeated pattern

from P_3_1 import apply_3_1_129

SUTRA_CODE = "प.3.1.129"
SUTRA_TEXT = "पाय्यसान्नाय्यनिकाय्यधाय्या मानहविर्निवाससामिधेनीषु"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — repeated pattern"


class Sutra31129:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_129(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.129:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.129:root=रामः;pos='),
		('सीता', '', 'प.3.1.129:root=सीता;pos='),
	]

