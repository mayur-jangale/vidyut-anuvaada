# Sutra प.3.2.113: न यदि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — na yadi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.113"
SUTRA_TEXT = "न यदि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — na yadi"


class Sutra32113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

