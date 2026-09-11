# Sutra प.3.3.83: स्तम्बे क च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambe ka ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.83"
SUTRA_TEXT = "स्तम्बे क च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambe ka ca"


class Sutra3383:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

