# Sutra प.1.2.13: वा गमः
# (Samjna (technical definitions)) — vA gamaH

from P_1_2 import apply_1_2_13

SUTRA_CODE = "प.1.2.13"
SUTRA_TEXT = "वा गमः"
SUTRA_DESC = "(Samjna (technical definitions)) — vA gamaH"


class Sutra1213:
	def apply(self, word, pos):
		return apply_1_2_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-gam:अग्निः'),
		('रामः', '', 'non-gam:रामः'),
		('सीता', '', 'non-gam:सीता'),
	]

