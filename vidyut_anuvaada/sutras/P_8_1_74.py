# Sutra प.8.1.74: विभाषितं विशेषवचने बहुवचनम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.74"
SUTRA_TEXT = "विभाषितं विशेषवचने बहुवचनम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.74: अग्निः'),
		('रामः', '', 'प.8.1.74: रामः'),
		('सीता', '', 'प.8.1.74: सीता'),
	]

