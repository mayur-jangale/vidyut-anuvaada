# Sutra प.3.2.95: राजनि युधिकृञः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — rAjani yuDikfYaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.95"
SUTRA_TEXT = "राजनि युधिकृञः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — rAjani yuDikfYaH"


class Sutra3295:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

