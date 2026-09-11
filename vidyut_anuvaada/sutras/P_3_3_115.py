# Sutra प.3.3.115: ल्युट् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lyuw ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.115"
SUTRA_TEXT = "ल्युट् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lyuw ca"


class Sutra33115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

