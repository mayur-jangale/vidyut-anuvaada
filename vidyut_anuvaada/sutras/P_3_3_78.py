# Sutra प.3.3.78: अन्तर्घनो देशे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — antarGano deSe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.78"
SUTRA_TEXT = "अन्तर्घनो देशे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — antarGano deSe"


class Sutra3378:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

