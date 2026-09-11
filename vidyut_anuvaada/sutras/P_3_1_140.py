# Sutra प.3.1.140: ज्वलितिकसन्तेभ्यो णः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — jvalitikasanteByo RaH

from P_3_1 import apply_3_1_140

SUTRA_CODE = "प.3.1.140"
SUTRA_TEXT = "ज्वलितिकसन्तेभ्यो णः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — jvalitikasanteByo RaH"


class Sutra31140:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_140(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.140:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.140:root=रामः;pos='),
		('सीता', '', 'प.3.1.140:root=सीता;pos='),
	]

