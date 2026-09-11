# Sutra प.3.3.30: कॄ धान्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kF DAnye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.30"
SUTRA_TEXT = "कॄ धान्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kF DAnye"


class Sutra3330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

