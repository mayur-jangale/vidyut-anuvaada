# Sutra प.3.3.88: ड्वितः क्त्रिः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — qvitaH ktriH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.88"
SUTRA_TEXT = "ड्वितः क्त्रिः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — qvitaH ktriH"


class Sutra3388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

