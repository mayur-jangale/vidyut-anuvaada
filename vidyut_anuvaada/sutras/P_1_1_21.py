# Sutra प.1.1.21: आद्यन्तवदेकस्मिन्
# (Samjna (technical definitions)) — Adyantavadekasmin

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.21"
SUTRA_TEXT = "आद्यन्तवदेकस्मिन्"
SUTRA_DESC = "(Samjna (technical definitions)) — Adyantavadekasmin"


class Sutra1121:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_21
		return apply_1_1_21(word, pos)

	EXAMPLES = [
		('अग्नि', '', 'first=last:अ/ि;word=अग्नि'),
		('देव', '', 'first=last:द/व;word=देव'),
	]

