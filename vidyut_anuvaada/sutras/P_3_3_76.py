# Sutra प.3.3.76: हनश्च वधः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — hanaSca vaDaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.76"
SUTRA_TEXT = "हनश्च वधः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — hanaSca vaDaH"


class Sutra3376:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

