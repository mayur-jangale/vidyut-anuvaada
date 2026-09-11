# Sutra प.1.4.8: पतिः समास एव
# (Samjna (technical definitions)) — patiH samAsa eva

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.8"
SUTRA_TEXT = "पतिः समास एव"
SUTRA_DESC = "(Samjna (technical definitions)) — patiH samAsa eva"


class Sutra148:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_8
		return apply_1_4_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-pati:अग्निः'),
		('रामः', '', 'not-pati:रामः'),
		('सीता', '', 'not-pati:सीता'),
	]

