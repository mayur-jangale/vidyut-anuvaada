# Sutra प.3.2.53: अमनुष्यकर्तृके च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — amanuzyakartfke ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.53"
SUTRA_TEXT = "अमनुष्यकर्तृके च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — amanuzyakartfke ca"


class Sutra3253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

