# Sutra प.8.1.60: हेति क्षियायाम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.60"
SUTRA_TEXT = "हेति क्षियायाम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.60: अग्निः'),
		('रामः', '', 'प.8.1.60: रामः'),
		('सीता', '', 'प.8.1.60: सीता'),
	]

