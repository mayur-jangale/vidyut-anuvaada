# Sutra प.3.2.156: प्रजोरिनिः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — prajoriniH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.156"
SUTRA_TEXT = "प्रजोरिनिः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — prajoriniH"


class Sutra32156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

