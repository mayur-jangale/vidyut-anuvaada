# Sutra प.1.4.82: व्यवहिताश्च
# (Samjna (technical definitions)) — vyavahitASca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.82"
SUTRA_TEXT = "व्यवहिताश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — vyavahitASca"


class Sutra1482:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_82
		return apply_1_4_82(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-vyavahita:अग्निः'),
		('रामः', '', 'not-vyavahita:रामः'),
		('सीता', '', 'not-vyavahita:सीता'),
	]

