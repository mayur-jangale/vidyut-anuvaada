# Sutra प.3.3.38: परावनुपात्यय इणः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parAvanupAtyaya iRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.38"
SUTRA_TEXT = "परावनुपात्यय इणः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parAvanupAtyaya iRaH"


class Sutra3338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

