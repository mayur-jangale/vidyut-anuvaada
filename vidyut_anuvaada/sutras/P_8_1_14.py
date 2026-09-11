# Sutra प.8.1.14: यथास्वे यथायथम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.14"
SUTRA_TEXT = "यथास्वे यथायथम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.14: अग्निः'),
		('रामः', '', 'प.8.1.14: रामः'),
		('सीता', '', 'प.8.1.14: सीता'),
	]

