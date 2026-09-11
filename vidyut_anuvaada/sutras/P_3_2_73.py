# Sutra प.3.2.73: विजुपे छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vijupe Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.73"
SUTRA_TEXT = "विजुपे छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vijupe Candasi"


class Sutra3273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

