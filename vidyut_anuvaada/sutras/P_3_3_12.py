# Sutra प.3.3.12: अण् कर्मणि च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aR karmaRi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.12"
SUTRA_TEXT = "अण् कर्मणि च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aR karmaRi ca"


class Sutra3312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

