# Sutra प.3.2.116: हशश्वतोर्लङ् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — haSaSvatorlaN ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.116"
SUTRA_TEXT = "हशश्वतोर्लङ् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — haSaSvatorlaN ca"


class Sutra32116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

