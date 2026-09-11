# Sutra प.3.2.5: तुन्दशोकयोः परिमृजापनुदोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tundaSokayoH parimfjApanudoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.5"
SUTRA_TEXT = "तुन्दशोकयोः परिमृजापनुदोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tundaSokayoH parimfjApanudoH"


class Sutra325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

