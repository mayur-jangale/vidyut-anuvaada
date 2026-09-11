# Sutra प.3.4.29: कर्मणि दृशिविदोः साकल्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRi dfSividoH sAkalye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.29"
SUTRA_TEXT = "कर्मणि दृशिविदोः साकल्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRi dfSividoH sAkalye"


class Sutra3429:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

