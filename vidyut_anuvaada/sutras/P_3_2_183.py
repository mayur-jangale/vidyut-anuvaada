# Sutra प.3.2.183: हलसूकरयोः पुवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — halasUkarayoH puvaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.183"
SUTRA_TEXT = "हलसूकरयोः पुवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — halasUkarayoH puvaH"


class Sutra32183:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

