# Sutra प.1.2.29: उच्चैरुदात्तः
# (Samjna (technical definitions)) — uccErudAttaH

from P_1_2 import apply_1_2_29

SUTRA_CODE = "प.1.2.29"
SUTRA_TEXT = "उच्चैरुदात्तः"
SUTRA_DESC = "(Samjna (technical definitions)) — uccErudAttaH"


class Sutra1229:
	def apply(self, word, pos):
		return apply_1_2_29(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-udātta:अग्निः'),
		('रामः', '', 'non-udātta:रामः'),
		('सीता', '', 'non-udātta:सीता'),
	]

