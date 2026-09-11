# Sutra प.6.2.108: क्षेपे
# (Sandhi (euphonic combination)) — kzepe

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.108"
SUTRA_TEXT = "क्षेपे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kzepe"


class Sutra62108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.108: अग्निः'),
		('रामः', '', 'प.6.2.108: रामः'),
		('सीता', '', 'प.6.2.108: सीता'),
	]

