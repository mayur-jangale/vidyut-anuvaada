# Sutra प.3.1.42: अभ्युत्सादयांप्रजनयांचिकयांरमयामकः पावयांक्रियाद्विदामक्रन्निति च्छन्दसि
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — aByutsAdayAMprajanayAMcikayAMramayAmakaH pAvayAMkriyAdvidAmakranniti cCandasi

from P_3_1 import apply_3_1_42

SUTRA_CODE = "प.3.1.42"
SUTRA_TEXT = "अभ्युत्सादयांप्रजनयांचिकयांरमयामकः पावयांक्रियाद्विदामक्रन्निति च्छन्दसि"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — aByutsAdayAMprajanayAMcikayAMramayAmakaH pAvayAMkriyAdvidAmakranniti cCandasi"


class Sutra3142:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.42:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.42:root=रामः;pos='),
		('सीता', '', 'प.3.1.42:root=सीता;pos='),
	]

