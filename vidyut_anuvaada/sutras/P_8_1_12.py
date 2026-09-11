# Sutra प.8.1.12: प्रकारे गुणवचनस्य
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.12"
SUTRA_TEXT = "प्रकारे गुणवचनस्य"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.12: अग्निः'),
		('रामः', '', 'प.8.1.12: रामः'),
		('सीता', '', 'प.8.1.12: सीता'),
	]

