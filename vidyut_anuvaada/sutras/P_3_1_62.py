# Sutra प.3.1.62: अचः कर्मकर्तरि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — acaH karmakartari

from P_3_1 import apply_3_1_62

SUTRA_CODE = "प.3.1.62"
SUTRA_TEXT = "अचः कर्मकर्तरि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — acaH karmakartari"


class Sutra3162:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.62:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.62:root=रामः;pos='),
		('सीता', '', 'प.3.1.62:root=सीता;pos='),
	]

