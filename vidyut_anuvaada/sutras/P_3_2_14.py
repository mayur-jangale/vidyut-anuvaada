# Sutra प.3.2.14: शमि धातोः संज्ञायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sami DAtoH saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.14"
SUTRA_TEXT = "शमि धातोः संज्ञायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sami DAtoH saMjYAyAm"


class Sutra3214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

