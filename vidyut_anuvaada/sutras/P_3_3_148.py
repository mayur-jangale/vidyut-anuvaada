# Sutra प.3.3.148: यच्चयत्रयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaccayatrayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.148"
SUTRA_TEXT = "यच्चयत्रयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaccayatrayoH"


class Sutra33148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

