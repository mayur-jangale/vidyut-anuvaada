# Sutra प.3.3.8: लोडर्थलक्षणे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — loqarTalakzaRe ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.8"
SUTRA_TEXT = "लोडर्थलक्षणे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — loqarTalakzaRe ca"


class Sutra338:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

