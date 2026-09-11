# Sutra प.3.1.32: सनाद्यन्ता धातवः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sanAdyantA DAtavaH

from P_3_1 import apply_3_1_32

SUTRA_CODE = "प.3.1.32"
SUTRA_TEXT = "सनाद्यन्ता धातवः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sanAdyantA DAtavaH"


class Sutra3132:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.32:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.32:root=रामः;pos='),
		('सीता', '', 'प.3.1.32:root=सीता;pos='),
	]

