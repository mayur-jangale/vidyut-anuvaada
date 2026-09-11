# Sutra प.8.1.72: आमन्त्रितं पूर्वमविद्यमानवत्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.72"
SUTRA_TEXT = "आमन्त्रितं पूर्वमविद्यमानवत्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.72: अग्निः'),
		('रामः', '', 'प.8.1.72: रामः'),
		('सीता', '', 'प.8.1.72: सीता'),
	]

