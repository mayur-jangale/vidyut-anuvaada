# Sutra प.3.2.10: वयसि च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vayasi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.10"
SUTRA_TEXT = "वयसि च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vayasi ca"


class Sutra3210:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

