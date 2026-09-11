# Sutra प.3.2.134: आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkvestacCIlatadDarmatatsADukArizu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.134"
SUTRA_TEXT = "आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — AkvestacCIlatadDarmatatsADukArizu"


class Sutra32134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

