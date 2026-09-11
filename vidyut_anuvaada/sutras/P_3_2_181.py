# Sutra प.3.2.181: धः कर्मणि ष्ट्रन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — DaH karmaRi zwran

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.181"
SUTRA_TEXT = "धः कर्मणि ष्ट्रन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — DaH karmaRi zwran"


class Sutra32181:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

