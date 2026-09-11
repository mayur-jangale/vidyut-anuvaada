# Sutra प.3.1.114: राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_114

SUTRA_CODE = "प.3.1.114"
SUTRA_TEXT = "राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra31114:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_114(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.114:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.114:root=रामः;pos='),
		('सीता', '', 'प.3.1.114:root=सीता;pos='),
	]

