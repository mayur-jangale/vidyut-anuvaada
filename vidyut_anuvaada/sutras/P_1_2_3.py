# Sutra प.1.2.3: विभाषोर्णोः
# (Samjna (technical definitions)) — viBAzorRoH

from P_1_2 import apply_1_2_3

SUTRA_CODE = "प.1.2.3"
SUTRA_TEXT = "विभाषोर्णोः"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzorRoH"


class Sutra123:
	def apply(self, word, pos):
		return apply_1_2_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-urṇau:अग्निः'),
		('रामः', '', 'non-urṇau:रामः'),
		('सीता', '', 'non-urṇau:सीता'),
	]

