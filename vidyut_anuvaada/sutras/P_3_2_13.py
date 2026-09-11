# Sutra प.3.2.13: स्तम्बकर्णयो रमिजपोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambakarRayo ramijapoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.13"
SUTRA_TEXT = "स्तम्बकर्णयो रमिजपोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — stambakarRayo ramijapoH"


class Sutra3213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

