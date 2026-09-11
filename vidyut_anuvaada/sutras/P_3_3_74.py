# Sutra प.3.3.74: निपानमाहावः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nipAnamAhAvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.74"
SUTRA_TEXT = "निपानमाहावः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nipAnamAhAvaH"


class Sutra3374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

