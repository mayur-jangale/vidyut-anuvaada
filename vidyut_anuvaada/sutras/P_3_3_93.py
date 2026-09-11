# Sutra प.3.3.93: कर्मण्यधिकरणे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyaDikaraRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.93"
SUTRA_TEXT = "कर्मण्यधिकरणे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyaDikaraRe ca"


class Sutra3393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

