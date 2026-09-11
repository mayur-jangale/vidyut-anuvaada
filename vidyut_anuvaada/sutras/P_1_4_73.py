# Sutra प.1.4.73: उपाजेऽन्वाजे
# (Samjna (technical definitions)) — upAje'nvAje

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.73"
SUTRA_TEXT = "उपाजेऽन्वाजे"
SUTRA_DESC = "(Samjna (technical definitions)) — upAje'nvAje"


class Sutra1473:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_73
		return apply_1_4_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-upAja:अग्निः'),
		('रामः', '', 'not-upAja:रामः'),
		('सीता', '', 'not-upAja:सीता'),
	]

