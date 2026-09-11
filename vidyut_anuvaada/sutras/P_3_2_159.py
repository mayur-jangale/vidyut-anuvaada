# Sutra प.3.2.159: दाधेट्सिशदसदो रुः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dADewsiSadasado ruH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.159"
SUTRA_TEXT = "दाधेट्सिशदसदो रुः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dADewsiSadasado ruH"


class Sutra32159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

