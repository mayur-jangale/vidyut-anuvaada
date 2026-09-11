# Sutra प.3.4.31: चर्मोदरयोः पूरेः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — carmodarayoH pUreH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.31"
SUTRA_TEXT = "चर्मोदरयोः पूरेः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — carmodarayoH pUreH"


class Sutra3431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

