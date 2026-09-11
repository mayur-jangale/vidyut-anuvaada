# Sutra प.8.1.18: अनुदात्तं सर्वमपादादौ
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.18"
SUTRA_TEXT = "अनुदात्तं सर्वमपादादौ"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.18: अग्निः'),
		('रामः', '', 'प.8.1.18: रामः'),
		('सीता', '', 'प.8.1.18: सीता'),
	]

