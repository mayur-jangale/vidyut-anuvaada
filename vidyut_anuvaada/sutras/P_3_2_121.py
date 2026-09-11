# Sutra प.3.2.121: नन्वोर्विभाषा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nanvorviBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.121"
SUTRA_TEXT = "नन्वोर्विभाषा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nanvorviBAzA"


class Sutra32121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

