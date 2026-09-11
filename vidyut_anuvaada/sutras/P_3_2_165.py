# Sutra प.3.2.165: जागुरूकः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAgurUkaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.165"
SUTRA_TEXT = "जागुरूकः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAgurUkaH"


class Sutra32165:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

