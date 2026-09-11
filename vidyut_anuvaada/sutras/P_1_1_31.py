# Sutra प.1.1.31: द्वन्द्वे च
# (Samjna (technical definitions)) — dvandve ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.31"
SUTRA_TEXT = "द्वन्द्वे च"
SUTRA_DESC = "(Samjna (technical definitions)) — dvandve ca"


class Sutra1131:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_31
		return apply_1_1_31(word, pos)

	EXAMPLES = [
		('नरनार', 'dvandva', 'dvandva:नरनार'),
		('देव', '', 'non-dvandva:देव'),
	]

