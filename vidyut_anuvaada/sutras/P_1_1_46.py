# Sutra प.1.1.46: आद्यन्तौ टकितौ
# (Samjna (technical definitions)) — AdyantO wakitO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.46"
SUTRA_TEXT = "आद्यन्तौ टकितौ"
SUTRA_DESC = "(Samjna (technical definitions)) — AdyantO wakitO"


class Sutra1146:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_46
		return apply_1_1_46(word, pos)

	EXAMPLES = [
		('टि', '', 'प.1.1.46:ādyantau-ṭakitau;input=टि'),
		('अग्नि', '', 'प.1.1.46:ādyantau-ṭakitau;input=अग्नि'),
	]

