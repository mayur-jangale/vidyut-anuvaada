# Sutra प.3.3.59: उपसर्गेऽदः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — upasarge'daH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.59"
SUTRA_TEXT = "उपसर्गेऽदः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — upasarge'daH"


class Sutra3359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

