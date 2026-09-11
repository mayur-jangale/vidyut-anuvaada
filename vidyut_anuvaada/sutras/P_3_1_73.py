# Sutra प.3.1.73: स्वादिभ्यः श्नुः
# śnābhyāṃ śnoḥ — alternative form

from P_3_1 import apply_3_1_73

SUTRA_CODE = "प.3.1.73"
SUTRA_TEXT = "स्वादिभ्यः श्नुः"
SUTRA_DESC = "śnābhyāṃ śnoḥ — alternative form"


class Sutra3173:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.73:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.73:root=रामः;pos='),
		('सीता', '', 'प.3.1.73:root=सीता;pos='),
	]

