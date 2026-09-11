# Sutra प.3.4.19: उदीचां माङो व्यतीहारे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — udIcAM mANo vyatIhAre

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.19"
SUTRA_TEXT = "उदीचां माङो व्यतीहारे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — udIcAM mANo vyatIhAre"


class Sutra3419:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

