# Sutra प.3.1.131: अग्नौ परिचाय्योपचाय्यसमूह्याः
# śāṅgyāḥ — repeated pattern

from P_3_1 import apply_3_1_131

SUTRA_CODE = "प.3.1.131"
SUTRA_TEXT = "अग्नौ परिचाय्योपचाय्यसमूह्याः"
SUTRA_DESC = "śāṅgyāḥ — repeated pattern"


class Sutra31131:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_131(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.131:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.131:root=रामः;pos='),
		('सीता', '', 'प.3.1.131:root=सीता;pos='),
	]

