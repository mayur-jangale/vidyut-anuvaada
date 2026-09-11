# Sutra प.3.2.85: करणे यजः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRe yajaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.85"
SUTRA_TEXT = "करणे यजः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRe yajaH"


class Sutra3285:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

