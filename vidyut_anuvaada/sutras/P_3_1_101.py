# Sutra प.3.1.101: अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु
# ṅitvasya — repeated pattern

from P_3_1 import apply_3_1_101

SUTRA_CODE = "प.3.1.101"
SUTRA_TEXT = "अवद्यपण्यवर्या गर्ह्यपणितव्यानिरोधेषु"
SUTRA_DESC = "ṅitvasya — repeated pattern"


class Sutra31101:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_101(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.101:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.101:root=रामः;pos='),
		('सीता', '', 'प.3.1.101:root=सीता;pos='),
	]

