# Sutra प.3.3.174: क्तिच्क्तौ च संज्ञायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kticktO ca saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.174"
SUTRA_TEXT = "क्तिच्क्तौ च संज्ञायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kticktO ca saMjYAyAm"


class Sutra33174:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

