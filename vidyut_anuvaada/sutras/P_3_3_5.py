# Sutra प.3.3.5: विभाषा कदाकर्ह्योः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA kadAkarhyoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.5"
SUTRA_TEXT = "विभाषा कदाकर्ह्योः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA kadAkarhyoH"


class Sutra335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

