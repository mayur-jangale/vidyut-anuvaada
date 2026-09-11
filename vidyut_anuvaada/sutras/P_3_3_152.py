# Sutra प.3.3.152: उताप्योः समर्थयोर्लिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — utApyoH samarTayorliN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.152"
SUTRA_TEXT = "उताप्योः समर्थयोर्लिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — utApyoH samarTayorliN"


class Sutra33152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

