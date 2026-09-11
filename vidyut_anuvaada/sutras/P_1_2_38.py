# Sutra प.1.2.38: देवब्रह्मणोरनुदात्तः
# (Samjna (technical definitions)) — devabrahmaRoranudAttaH

from P_1_2 import apply_1_2_38

SUTRA_CODE = "प.1.2.38"
SUTRA_TEXT = "देवब्रह्मणोरनुदात्तः"
SUTRA_DESC = "(Samjna (technical definitions)) — devabrahmaRoranudAttaH"


class Sutra1238:
	def apply(self, word, pos):
		return apply_1_2_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-deva-brahma:अग्निः'),
		('रामः', '', 'non-deva-brahma:रामः'),
		('सीता', '', 'non-deva-brahma:सीता'),
	]

