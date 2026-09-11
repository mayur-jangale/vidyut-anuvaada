# Sutra प.3.3.87: निघो निमितम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — niGo nimitam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.87"
SUTRA_TEXT = "निघो निमितम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — niGo nimitam"


class Sutra3387:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

