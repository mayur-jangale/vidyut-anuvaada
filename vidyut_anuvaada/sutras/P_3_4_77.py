# Sutra प.3.4.77: लस्य
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lasya

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.77"
SUTRA_TEXT = "लस्य"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lasya"


class Sutra3477:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

