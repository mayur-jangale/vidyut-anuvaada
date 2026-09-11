# Sutra प.3.3.143: विभाषा कथमि लिङ् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA kaTami liN ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.143"
SUTRA_TEXT = "विभाषा कथमि लिङ् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA kaTami liN ca"


class Sutra33143:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

