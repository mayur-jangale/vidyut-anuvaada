# Sutra प.3.1.148: हश्च व्रीहिकालयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — haSca vrIhikAlayoH

from P_3_1 import apply_3_1_148

SUTRA_CODE = "प.3.1.148"
SUTRA_TEXT = "हश्च व्रीहिकालयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — haSca vrIhikAlayoH"


class Sutra31148:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_148(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.148:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.148:root=रामः;pos='),
		('सीता', '', 'प.3.1.148:root=सीता;pos='),
	]

