# Sutra प.3.3.22: उपसर्गे रुवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — upasarge ruvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.22"
SUTRA_TEXT = "उपसर्गे रुवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — upasarge ruvaH"


class Sutra3322:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

