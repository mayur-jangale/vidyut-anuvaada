# Sutra प.8.1.32: सत्यं प्रश्ने
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.32"
SUTRA_TEXT = "सत्यं प्रश्ने"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.32: अग्निः'),
		('रामः', '', 'प.8.1.32: रामः'),
		('सीता', '', 'प.8.1.32: सीता'),
	]

