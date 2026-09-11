# Sutra प.3.2.112: अभिज्ञावचने लृट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aBijYAvacane lfw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.112"
SUTRA_TEXT = "अभिज्ञावचने लृट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aBijYAvacane lfw"


class Sutra32112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

