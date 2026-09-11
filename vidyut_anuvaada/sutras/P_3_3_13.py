# Sutra प.3.3.13: लृट् शेषे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lfw Seze ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.13"
SUTRA_TEXT = "लृट् शेषे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lfw Seze ca"


class Sutra3313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

