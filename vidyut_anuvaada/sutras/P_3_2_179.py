# Sutra प.3.2.179: भुवः संज्ञाऽन्तरयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BuvaH saMjYA'ntarayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.179"
SUTRA_TEXT = "भुवः संज्ञाऽन्तरयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BuvaH saMjYA'ntarayoH"


class Sutra32179:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

