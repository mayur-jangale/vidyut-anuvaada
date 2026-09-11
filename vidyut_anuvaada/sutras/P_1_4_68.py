# Sutra प.1.4.68: अस्तं च
# (Samjna (technical definitions)) — astaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.68"
SUTRA_TEXT = "अस्तं च"
SUTRA_DESC = "(Samjna (technical definitions)) — astaM ca"


class Sutra1468:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_68
		return apply_1_4_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-astaM:अग्निः'),
		('रामः', '', 'not-astaM:रामः'),
		('सीता', '', 'not-astaM:सीता'),
	]

