# Sutra प.3.1.46: श्लिष आलिङ्गने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sliza AliNgane

from P_3_1 import apply_3_1_46

SUTRA_CODE = "प.3.1.46"
SUTRA_TEXT = "श्लिष आलिङ्गने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sliza AliNgane"


class Sutra3146:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.46:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.46:root=रामः;pos='),
		('सीता', '', 'प.3.1.46:root=सीता;pos='),
	]

