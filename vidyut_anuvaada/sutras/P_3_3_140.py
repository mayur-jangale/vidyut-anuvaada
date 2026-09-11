# Sutra प.3.3.140: भूते च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.140"
SUTRA_TEXT = "भूते च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte ca"


class Sutra33140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

