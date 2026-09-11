# Sutra प.3.3.160: इच्छार्थेभ्यो विभाषा वर्तमाने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — icCArTeByo viBAzA vartamAne

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.160"
SUTRA_TEXT = "इच्छार्थेभ्यो विभाषा वर्तमाने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — icCArTeByo viBAzA vartamAne"


class Sutra33160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

