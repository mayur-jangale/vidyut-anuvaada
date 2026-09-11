# Sutra प.3.1.78: रुधादिभ्यः श्नम्
# śāṅgyāḥ — śāṅ suffix rules

from P_3_1 import apply_3_1_78

SUTRA_CODE = "प.3.1.78"
SUTRA_TEXT = "रुधादिभ्यः श्नम्"
SUTRA_DESC = "śāṅgyāḥ — śāṅ suffix rules"


class Sutra3178:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_78(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.78:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.78:root=रामः;pos='),
		('सीता', '', 'प.3.1.78:root=सीता;pos='),
	]

