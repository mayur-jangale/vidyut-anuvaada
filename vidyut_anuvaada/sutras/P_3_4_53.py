# Sutra प.3.4.53: द्वितीयायां च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — dvitIyAyAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.53"
SUTRA_TEXT = "द्वितीयायां च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — dvitIyAyAM ca"


class Sutra3453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

