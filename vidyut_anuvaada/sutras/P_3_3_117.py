# Sutra प.3.3.117: करणाधिकरणयोश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRADikaraRayoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.117"
SUTRA_TEXT = "करणाधिकरणयोश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRADikaraRayoSca"


class Sutra33117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

