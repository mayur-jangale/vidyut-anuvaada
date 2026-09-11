# Sutra प.1.4.108: शेषे प्रथमः
# (Samjna (technical definitions)) — Seze praTamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.108"
SUTRA_TEXT = "शेषे प्रथमः"
SUTRA_DESC = "(Samjna (technical definitions)) — Seze praTamaH"


class Sutra14108:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_108
		return apply_1_4_108(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'pada:prathama:default;word=अग्निः'),
		('रामः', '', 'pada:prathama:default;word=रामः'),
		('सीता', '', 'pada:prathama:default;word=सीता'),
	]

