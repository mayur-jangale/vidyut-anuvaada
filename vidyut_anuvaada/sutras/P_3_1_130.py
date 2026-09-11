# Sutra प.3.1.130: क्रतौ कुण्डपाय्यसंचाय्यौ
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_130

SUTRA_CODE = "प.3.1.130"
SUTRA_TEXT = "क्रतौ कुण्डपाय्यसंचाय्यौ"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra31130:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_130(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.130:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.130:root=रामः;pos='),
		('सीता', '', 'प.3.1.130:root=सीता;pos='),
	]

