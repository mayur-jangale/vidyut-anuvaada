# Sutra प.1.2.12: उश्च
# (Samjna (technical definitions)) — uSca

from P_1_2 import apply_1_2_12

SUTRA_CODE = "प.1.2.12"
SUTRA_TEXT = "उश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — uSca"


class Sutra1212:
	def apply(self, word, pos):
		return apply_1_2_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-u:अग्निः'),
		('रामः', '', 'no-u:रामः'),
		('सीता', '', 'no-u:सीता'),
	]

