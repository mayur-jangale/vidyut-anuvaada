# Sutra प.3.4.34: निमूलसमूलयोः कषः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nimUlasamUlayoH kazaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.34"
SUTRA_TEXT = "निमूलसमूलयोः कषः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nimUlasamUlayoH kazaH"


class Sutra3434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

