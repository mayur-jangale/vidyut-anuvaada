# Sutra प.3.1.34: सिब्बहुलं लेटि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sibbahulaM lewi

from P_3_1 import apply_3_1_34

SUTRA_CODE = "प.3.1.34"
SUTRA_TEXT = "सिब्बहुलं लेटि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sibbahulaM lewi"


class Sutra3134:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.34:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.34:root=रामः;pos='),
		('सीता', '', 'प.3.1.34:root=सीता;pos='),
	]

