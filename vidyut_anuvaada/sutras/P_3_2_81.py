# Sutra प.3.2.81: बहुलमाभीक्ष्ण्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — bahulamABIkzRye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.81"
SUTRA_TEXT = "बहुलमाभीक्ष्ण्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — bahulamABIkzRye"


class Sutra3281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

