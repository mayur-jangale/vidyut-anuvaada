# Sutra प.1.4.86: हीने
# (Samjna (technical definitions)) — hIne

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.86"
SUTRA_TEXT = "हीने"
SUTRA_DESC = "(Samjna (technical definitions)) — hIne"


class Sutra1486:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_86
		return apply_1_4_86(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-hIna:अग्निः'),
		('रामः', '', 'not-hIna:रामः'),
		('सीता', '', 'not-hIna:सीता'),
	]

