# Sutra प.3.3.44: अभिविधौ भाव इनुण्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aBiviDO BAva inuR

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.44"
SUTRA_TEXT = "अभिविधौ भाव इनुण्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aBiviDO BAva inuR"


class Sutra3344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

