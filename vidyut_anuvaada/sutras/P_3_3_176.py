# Sutra प.3.3.176: स्मोत्तरे लङ् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — smottare laN ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.176"
SUTRA_TEXT = "स्मोत्तरे लङ् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — smottare laN ca"


class Sutra33176:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

