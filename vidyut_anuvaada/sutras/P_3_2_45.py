# Sutra प.3.2.45: आशिते भुवः करणभावयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASite BuvaH karaRaBAvayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.45"
SUTRA_TEXT = "आशिते भुवः करणभावयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ASite BuvaH karaRaBAvayoH"


class Sutra3245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

