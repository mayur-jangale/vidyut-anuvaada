# Sutra प.1.4.79: जीविकोपनिषदावौपम्ये
# (Samjna (technical definitions)) — jIvikopanizadAvOpamye

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.79"
SUTRA_TEXT = "जीविकोपनिषदावौपम्ये"
SUTRA_DESC = "(Samjna (technical definitions)) — jIvikopanizadAvOpamye"


class Sutra1479:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_79
		return apply_1_4_79(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-Opamya:अग्निः'),
		('रामः', '', 'not-Opamya:रामः'),
		('सीता', '', 'not-Opamya:सीता'),
	]

