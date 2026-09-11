# Sutra प.3.4.16: भावलक्षणे स्थेण्कृञ्वदिचरिहुतमिजनिभ्यस्तोसुन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAvalakzaRe sTeRkfYvadicarihutamijaniByastosun

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.16"
SUTRA_TEXT = "भावलक्षणे स्थेण्कृञ्वदिचरिहुतमिजनिभ्यस्तोसुन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAvalakzaRe sTeRkfYvadicarihutamijaniByastosun"


class Sutra3416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

