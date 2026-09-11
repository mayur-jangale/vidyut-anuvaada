# Sutra प.1.1.75: एङ् प्राचां देशे
# (Samjna (technical definitions)) — eN prAcAM deSe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.75"
SUTRA_TEXT = "एङ् प्राचां देशे"
SUTRA_DESC = "(Samjna (technical definitions)) — eN prAcAM deSe"


class Sutra1175:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_75
		return apply_1_1_75(word, pos)

	EXAMPLES = [
		('एङ्', '', 'प.1.1.75:eṅ-prācāṃ-deśe;input=एङ्'),
		('अग्नि', '', 'प.1.1.75:eṅ-prācāṃ-deśe;input=अग्नि'),
	]

