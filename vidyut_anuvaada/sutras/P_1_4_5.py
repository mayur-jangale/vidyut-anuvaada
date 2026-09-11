# Sutra प.1.4.5: वाऽऽमि
# (Samjna (technical definitions)) — vA''mi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.5"
SUTRA_TEXT = "वाऽऽमि"
SUTRA_DESC = "(Samjna (technical definitions)) — vA''mi"


class Sutra145:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_5
		return apply_1_4_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-opt-i:अग्निः'),
		('रामः', '', 'no-opt-i:रामः'),
		('सीता', '', 'no-opt-i:सीता'),
	]

