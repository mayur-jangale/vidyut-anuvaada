# Sutra प.6.2.195: सोरवक्षेपणे
# (Sandhi (euphonic combination)) — soravakzepaRe

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.195"
SUTRA_TEXT = "सोरवक्षेपणे"
SUTRA_DESC = "(Sandhi (euphonic combination)) — soravakzepaRe"


class Sutra62195:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.195: अग्निः'),
		('रामः', '', 'प.6.2.195: रामः'),
		('सीता', '', 'प.6.2.195: सीता'),
	]

