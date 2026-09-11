# Sutra प.3.4.41: अधिकरणे बन्धः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aDikaraRe banDaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.41"
SUTRA_TEXT = "अधिकरणे बन्धः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aDikaraRe banDaH"


class Sutra3441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

