# Sutra प.1.1.25: डति च
# (Samjna (technical definitions)) — qati ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.25"
SUTRA_TEXT = "डति च"
SUTRA_DESC = "(Samjna (technical definitions)) — qati ca"


class Sutra1125:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_25
		return apply_1_1_25(word, pos)

	EXAMPLES = [
		('डत्', '', 'non-ḍat:डत्'),
		('दश', '', 'non-ḍat:दश'),
	]

