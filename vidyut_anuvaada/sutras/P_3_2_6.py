# Sutra प.3.2.6: प्रे दाज्ञः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre dAjYaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.6"
SUTRA_TEXT = "प्रे दाज्ञः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — pre dAjYaH"


class Sutra326:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

