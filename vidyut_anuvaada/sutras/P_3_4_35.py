# Sutra प.3.4.35: शुष्कचूर्णरूक्षेषु पिषः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — SuzkacUrRarUkzezu pizaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.35"
SUTRA_TEXT = "शुष्कचूर्णरूक्षेषु पिषः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — SuzkacUrRarUkzezu pizaH"


class Sutra3435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

