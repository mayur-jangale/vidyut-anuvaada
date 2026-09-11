# Sutra प.3.3.60: नौ ण च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO Ra ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.60"
SUTRA_TEXT = "नौ ण च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO Ra ca"


class Sutra3360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

