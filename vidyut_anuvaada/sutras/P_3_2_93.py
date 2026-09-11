# Sutra प.3.2.93: कर्मणीनिविक्रियः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRInivikriyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.93"
SUTRA_TEXT = "कर्मणीनिविक्रियः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRInivikriyaH"


class Sutra3293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

