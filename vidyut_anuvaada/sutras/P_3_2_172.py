# Sutra प.3.2.172: स्वपितृषोर्नजिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — svapitfzornajiN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.172"
SUTRA_TEXT = "स्वपितृषोर्नजिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — svapitfzornajiN"


class Sutra32172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

