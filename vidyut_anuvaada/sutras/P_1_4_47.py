# Sutra प.1.4.47: अभिनिविशश्च
# (Samjna (technical definitions)) — aBiniviSaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.47"
SUTRA_TEXT = "अभिनिविशश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — aBiniviSaSca"


class Sutra1447:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_47
		return apply_1_4_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-abhiniviS-karman:अग्निः'),
		('रामः', '', 'not-abhiniviS-karman:रामः'),
		('सीता', '', 'not-abhiniviS-karman:सीता'),
	]

