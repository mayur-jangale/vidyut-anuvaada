# Sutra प.3.3.33: प्रथने वावशब्दे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — praTane vAvaSabde

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.33"
SUTRA_TEXT = "प्रथने वावशब्दे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — praTane vAvaSabde"


class Sutra3333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

