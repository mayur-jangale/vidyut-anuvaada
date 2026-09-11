# Sutra प.3.1.36: इजादेश्च गुरुमतोऽनृच्छः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ijAdeSca gurumato'nfcCaH

from P_3_1 import apply_3_1_36

SUTRA_CODE = "प.3.1.36"
SUTRA_TEXT = "इजादेश्च गुरुमतोऽनृच्छः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ijAdeSca gurumato'nfcCaH"


class Sutra3136:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_36(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.36:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.36:root=रामः;pos='),
		('सीता', '', 'प.3.1.36:root=सीता;pos='),
	]

