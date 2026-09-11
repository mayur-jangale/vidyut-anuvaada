# Sutra प.8.1.48: किम्वृत्तं च चिदुत्तरम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.48"
SUTRA_TEXT = "किम्वृत्तं च चिदुत्तरम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.48: अग्निः'),
		('रामः', '', 'प.8.1.48: रामः'),
		('सीता', '', 'प.8.1.48: सीता'),
	]

