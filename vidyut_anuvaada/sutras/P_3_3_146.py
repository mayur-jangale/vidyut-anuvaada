# Sutra प.3.3.146: किंकिलास्त्यर्थेषु लृट्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kiMkilAstyarTezu lfw

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.146"
SUTRA_TEXT = "किंकिलास्त्यर्थेषु लृट्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kiMkilAstyarTezu lfw"


class Sutra33146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

