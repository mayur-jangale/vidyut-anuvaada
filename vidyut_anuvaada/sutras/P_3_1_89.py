# Sutra प.3.1.89: न दुहस्नुनमां यक्चिणौ
# saṃyogaśiṣṭaḥ — consonant cluster rules

from P_3_1 import apply_3_1_89

SUTRA_CODE = "प.3.1.89"
SUTRA_TEXT = "न दुहस्नुनमां यक्चिणौ"
SUTRA_DESC = "saṃyogaśiṣṭaḥ — consonant cluster rules"


class Sutra3189:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_89(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.89:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.89:root=रामः;pos='),
		('सीता', '', 'प.3.1.89:root=सीता;pos='),
	]

