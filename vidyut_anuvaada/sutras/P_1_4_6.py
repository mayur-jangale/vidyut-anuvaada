# Sutra प.1.4.6: ङिति ह्रस्वश्च
# (Samjna (technical definitions)) — Niti hrasvaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.6"
SUTRA_TEXT = "ङिति ह्रस्वश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — Niti hrasvaSca"


class Sutra146:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_6
		return apply_1_4_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-Nit:अग्निः'),
		('रामः', '', 'no-Nit:रामः'),
		('सीता', '', 'no-Nit:सीता'),
	]

