# Sutra प.1.1.22: तरप्तमपौ घः
# (Samjna (technical definitions)) — taraptamapO GaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.22"
SUTRA_TEXT = "तरप्तमपौ घः"
SUTRA_DESC = "(Samjna (technical definitions)) — taraptamapO GaH"


class Sutra1122:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_22
		return apply_1_1_22(word, pos)

	EXAMPLES = [
		('श्रेष्ठतर', '', 'comparative:श्रेष्ठतर'),
		('अग्नि', '', 'non-comp:अग्नि'),
	]

