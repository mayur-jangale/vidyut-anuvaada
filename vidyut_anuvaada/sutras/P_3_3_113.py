# Sutra प.3.3.113: कृत्यल्युटो बहुलम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyalyuwo bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.113"
SUTRA_TEXT = "कृत्यल्युटो बहुलम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kftyalyuwo bahulam"


class Sutra33113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

