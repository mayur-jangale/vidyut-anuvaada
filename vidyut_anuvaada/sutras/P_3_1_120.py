# Sutra प.3.1.120: विभाषा कृवृषोः
# vali lopaḥ — repeated pattern

from P_3_1 import apply_3_1_120

SUTRA_CODE = "प.3.1.120"
SUTRA_TEXT = "विभाषा कृवृषोः"
SUTRA_DESC = "vali lopaḥ — repeated pattern"


class Sutra31120:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_120(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.120:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.120:root=रामः;pos='),
		('सीता', '', 'प.3.1.120:root=सीता;pos='),
	]

