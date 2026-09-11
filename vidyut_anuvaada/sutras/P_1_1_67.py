# Sutra प.1.1.67: तस्मादित्युत्तरस्य
# (Samjna (technical definitions)) — tasmAdityuttarasya

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.67"
SUTRA_TEXT = "तस्मादित्युत्तरस्य"
SUTRA_DESC = "(Samjna (technical definitions)) — tasmAdityuttarasya"


class Sutra1167:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_67
		return apply_1_1_67(word, pos)

	EXAMPLES = [
		('देव', '', 'following-element-applied:देव'),
	]

