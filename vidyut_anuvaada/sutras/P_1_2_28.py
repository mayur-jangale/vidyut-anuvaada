# Sutra प.1.2.28: अचश्च
# (Samjna (technical definitions)) — acaSca

from P_1_2 import apply_1_2_28

SUTRA_CODE = "प.1.2.28"
SUTRA_TEXT = "अचश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — acaSca"


class Sutra1228:
	def apply(self, word, pos):
		return apply_1_2_28(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'acaḥ:1-vowels=अ'),
		('रामः', '', 'acaḥ:0-vowels=none'),
		('सीता', '', 'acaḥ:0-vowels=none'),
	]

