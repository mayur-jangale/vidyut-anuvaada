# Sutra प.3.1.44: च्लेः सिच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — cleH sic

from P_3_1 import apply_3_1_44

SUTRA_CODE = "प.3.1.44"
SUTRA_TEXT = "च्लेः सिच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — cleH sic"


class Sutra3144:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.44:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.44:root=रामः;pos='),
		('सीता', '', 'प.3.1.44:root=सीता;pos='),
	]

