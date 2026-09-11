# Sutra प.3.3.141: वोताप्योः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — votApyoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.141"
SUTRA_TEXT = "वोताप्योः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — votApyoH"


class Sutra33141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

