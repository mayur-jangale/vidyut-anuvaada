# Sutra प.3.4.1: धातुसम्बन्धे प्रत्ययाः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtusambanDe pratyayAH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.1"
SUTRA_TEXT = "धातुसम्बन्धे प्रत्ययाः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtusambanDe pratyayAH"


class Sutra341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

