# Sutra प.3.3.65: क्वणो वीणायां च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kvaRo vIRAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.65"
SUTRA_TEXT = "क्वणो वीणायां च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kvaRo vIRAyAM ca"


class Sutra3365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

