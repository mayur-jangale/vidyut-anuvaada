# Sutra प.3.3.147: जातुयदोर्लिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAtuyadorliN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.147"
SUTRA_TEXT = "जातुयदोर्लिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jAtuyadorliN"


class Sutra33147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

