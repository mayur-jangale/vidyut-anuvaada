# Sutra प.1.4.64: भूषणेऽलम्
# (Samjna (technical definitions)) — BUzaRe'lam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.64"
SUTRA_TEXT = "भूषणेऽलम्"
SUTRA_DESC = "(Samjna (technical definitions)) — BUzaRe'lam"


class Sutra1464:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_64
		return apply_1_4_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-alam:अग्निः'),
		('रामः', '', 'not-alam:रामः'),
		('सीता', '', 'not-alam:सीता'),
	]

