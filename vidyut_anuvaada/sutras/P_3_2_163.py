# Sutra प.3.2.163: इण्नश्जिसर्त्तिभ्यः क्वरप्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — iRnaSjisarttiByaH kvarap

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.163"
SUTRA_TEXT = "इण्नश्जिसर्त्तिभ्यः क्वरप्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — iRnaSjisarttiByaH kvarap"


class Sutra32163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

