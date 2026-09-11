# Sutra प.3.3.100: कृञः श च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfYaH Sa ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.100"
SUTRA_TEXT = "कृञः श च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kfYaH Sa ca"


class Sutra33100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

