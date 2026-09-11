# Sutra प.3.1.33: स्यतासी लृलुटोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — syatAsI lfluwoH

from P_3_1 import apply_3_1_33

SUTRA_CODE = "प.3.1.33"
SUTRA_TEXT = "स्यतासी लृलुटोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — syatAsI lfluwoH"


class Sutra3133:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.33:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.33:root=रामः;pos='),
		('सीता', '', 'प.3.1.33:root=सीता;pos='),
	]

