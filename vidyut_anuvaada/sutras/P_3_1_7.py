# Sutra प.3.1.7: धातोः कर्मणः समानकर्तृकादिच्छायां वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtoH karmaRaH samAnakartfkAdicCAyAM vA

from P_3_1 import apply_3_1_7

SUTRA_CODE = "प.3.1.7"
SUTRA_TEXT = "धातोः कर्मणः समानकर्तृकादिच्छायां वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — DAtoH karmaRaH samAnakartfkAdicCAyAM vA"


class Sutra317:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.7:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.7:root=रामः;pos='),
		('सीता', '', 'प.3.1.7:root=सीता;pos='),
	]

