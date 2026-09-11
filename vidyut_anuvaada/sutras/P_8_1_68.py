# Sutra प.8.1.68: सगतिरपि तिङ्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.68"
SUTRA_TEXT = "सगतिरपि तिङ्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.68: अग्निः'),
		('रामः', '', 'प.8.1.68: रामः'),
		('सीता', '', 'प.8.1.68: सीता'),
	]

