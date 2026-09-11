# Sutra प.3.1.65: तपोऽनुतापे च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — tapo'nutApe ca

from P_3_1 import apply_3_1_65

SUTRA_CODE = "प.3.1.65"
SUTRA_TEXT = "तपोऽनुतापे च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — tapo'nutApe ca"


class Sutra3165:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.65:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.65:root=रामः;pos='),
		('सीता', '', 'प.3.1.65:root=सीता;pos='),
	]

