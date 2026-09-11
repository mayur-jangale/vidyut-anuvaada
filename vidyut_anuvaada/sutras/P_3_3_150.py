# Sutra प.3.3.150: चित्रीकरणे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — citrIkaraRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.150"
SUTRA_TEXT = "चित्रीकरणे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — citrIkaraRe ca"


class Sutra33150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

