# Sutra प.3.3.124: जालमानायः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAlamAnAyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.124"
SUTRA_TEXT = "जालमानायः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAlamAnAyaH"


class Sutra33124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

