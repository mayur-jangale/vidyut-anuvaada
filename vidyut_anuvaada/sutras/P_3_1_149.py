# Sutra प.3.1.149: प्रुसृल्वः समभिहारे वुन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — prusflvaH samaBihAre vun

from P_3_1 import apply_3_1_149

SUTRA_CODE = "प.3.1.149"
SUTRA_TEXT = "प्रुसृल्वः समभिहारे वुन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — prusflvaH samaBihAre vun"


class Sutra31149:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_149(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.149:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.149:root=रामः;pos='),
		('सीता', '', 'प.3.1.149:root=सीता;pos='),
	]

