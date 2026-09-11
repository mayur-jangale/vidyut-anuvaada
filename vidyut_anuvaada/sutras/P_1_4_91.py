# Sutra प.1.4.91: अभिरभागे
# (Samjna (technical definitions)) — aBiraBAge

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.91"
SUTRA_TEXT = "अभिरभागे"
SUTRA_DESC = "(Samjna (technical definitions)) — aBiraBAge"


class Sutra1491:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_91
		return apply_1_4_91(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-abhi-BAga:अग्निः'),
		('रामः', '', 'not-abhi-BAga:रामः'),
		('सीता', '', 'not-abhi-BAga:सीता'),
	]

