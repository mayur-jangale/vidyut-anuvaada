# Sutra प.1.2.30: नीचैरनुदात्तः
# (Samjna (technical definitions)) — nIcEranudAttaH

from P_1_2 import apply_1_2_30

SUTRA_CODE = "प.1.2.30"
SUTRA_TEXT = "नीचैरनुदात्तः"
SUTRA_DESC = "(Samjna (technical definitions)) — nIcEranudAttaH"


class Sutra1230:
	def apply(self, word, pos):
		return apply_1_2_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-anudātta:अग्निः'),
		('रामः', '', 'non-anudātta:रामः'),
		('सीता', '', 'non-anudātta:सीता'),
	]

