# Sutra प.3.3.132: आशंसायां भूतवच्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASaMsAyAM BUtavacca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.132"
SUTRA_TEXT = "आशंसायां भूतवच्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASaMsAyAM BUtavacca"


class Sutra33132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

