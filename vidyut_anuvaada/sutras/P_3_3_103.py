# Sutra प.3.3.103: गुरोश्च हलः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — guroSca halaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.103"
SUTRA_TEXT = "गुरोश्च हलः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — guroSca halaH"


class Sutra33103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

