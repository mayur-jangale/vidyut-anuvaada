# Sutra प.3.1.70: वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः
# śnābhyāṃ śnoḥ — ś and ñ become ṣṇ before certain endings

from P_3_1 import apply_3_1_70

SUTRA_CODE = "प.3.1.70"
SUTRA_TEXT = "वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः"
SUTRA_DESC = "śnābhyāṃ śnoḥ — ś and ñ become ṣṇ before certain endings"


class Sutra3170:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.70:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.70:root=रामः;pos='),
		('सीता', '', 'प.3.1.70:root=सीता;pos='),
	]

