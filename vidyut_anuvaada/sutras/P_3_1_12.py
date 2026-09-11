# Sutra प.3.1.12: भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BfSAdiByo BuvyacverlopaSca halaH

from P_3_1 import apply_3_1_12

SUTRA_CODE = "प.3.1.12"
SUTRA_TEXT = "भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BfSAdiByo BuvyacverlopaSca halaH"


class Sutra3112:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.12:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.12:root=रामः;pos='),
		('सीता', '', 'प.3.1.12:root=सीता;pos='),
	]

