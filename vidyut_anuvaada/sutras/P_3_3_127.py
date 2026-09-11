# Sutra प.3.3.127: कर्तृकर्मणोश्च भूकृञोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartfkarmaRoSca BUkfYoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.127"
SUTRA_TEXT = "कर्तृकर्मणोश्च भूकृञोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartfkarmaRoSca BUkfYoH"


class Sutra33127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

