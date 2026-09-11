# Sutra प.8.1.16: पदस्य
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.16"
SUTRA_TEXT = "पदस्य"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.16: अग्निः'),
		('रामः', '', 'प.8.1.16: रामः'),
		('सीता', '', 'प.8.1.16: सीता'),
	]

