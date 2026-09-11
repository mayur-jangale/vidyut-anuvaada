# Sutra प.3.2.7: समि ख्यः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sami KyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.7"
SUTRA_TEXT = "समि ख्यः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sami KyaH"


class Sutra327:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

