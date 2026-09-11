# Sutra प.3.3.89: ट्वितोऽथुच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — wvito'Tuc

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.89"
SUTRA_TEXT = "ट्वितोऽथुच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — wvito'Tuc"


class Sutra3389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

