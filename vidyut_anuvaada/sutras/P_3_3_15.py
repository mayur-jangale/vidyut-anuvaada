# Sutra प.3.3.15: अनद्यतने लुट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anadyatane luw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.15"
SUTRA_TEXT = "अनद्यतने लुट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anadyatane luw"


class Sutra3315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

