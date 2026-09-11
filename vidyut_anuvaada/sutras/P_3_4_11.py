# Sutra प.3.4.11: दृशे विख्ये च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dfSe viKye ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.11"
SUTRA_TEXT = "दृशे विख्ये च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dfSe viKye ca"


class Sutra3411:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

