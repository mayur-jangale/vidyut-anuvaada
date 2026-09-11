# Sutra प.3.4.26: स्वादुमि णमुल्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — svAdumi Ramul

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.26"
SUTRA_TEXT = "स्वादुमि णमुल्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — svAdumi Ramul"


class Sutra3426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

