# Sutra प.3.1.16: बाष्पोष्मभ्यामुद्वमने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — bAzpozmaByAmudvamane

from P_3_1 import apply_3_1_16

SUTRA_CODE = "प.3.1.16"
SUTRA_TEXT = "बाष्पोष्मभ्यामुद्वमने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — bAzpozmaByAmudvamane"


class Sutra3116:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.16:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.16:root=रामः;pos='),
		('सीता', '', 'प.3.1.16:root=सीता;pos='),
	]

