# Sutra प.3.2.166: यजजपदशां यङः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yajajapadaSAM yaNaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.166"
SUTRA_TEXT = "यजजपदशां यङः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yajajapadaSAM yaNaH"


class Sutra32166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

