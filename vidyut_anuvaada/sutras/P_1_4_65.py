# Sutra प.1.4.65: अन्तरपरिग्रहे
# (Samjna (technical definitions)) — antaraparigrahe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.65"
SUTRA_TEXT = "अन्तरपरिग्रहे"
SUTRA_DESC = "(Samjna (technical definitions)) — antaraparigrahe"


class Sutra1465:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_65
		return apply_1_4_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-antara:अग्निः'),
		('रामः', '', 'not-antara:रामः'),
		('सीता', '', 'not-antara:सीता'),
	]

