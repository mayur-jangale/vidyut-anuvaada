# Sutra प.1.4.16: सिति च
# (Samjna (technical definitions)) — siti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.16"
SUTRA_TEXT = "सिति च"
SUTRA_DESC = "(Samjna (technical definitions)) — siti ca"


class Sutra1416:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_16
		return apply_1_4_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-apply:अग्निः'),
		('रामः', '', 'no-apply:रामः'),
		('सीता', '', 'no-apply:सीता'),
	]

