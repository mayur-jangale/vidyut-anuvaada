# Sutra प.3.3.86: संघोद्घौ गणप्रशंसयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMGodGO gaRapraSaMsayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.86"
SUTRA_TEXT = "संघोद्घौ गणप्रशंसयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMGodGO gaRapraSaMsayoH"


class Sutra3386:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

