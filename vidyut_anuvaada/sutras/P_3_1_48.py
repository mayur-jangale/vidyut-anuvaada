# Sutra प.3.1.48: णिश्रिद्रुस्रुभ्यः कर्तरि चङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — RiSridrusruByaH kartari caN

from P_3_1 import apply_3_1_48

SUTRA_CODE = "प.3.1.48"
SUTRA_TEXT = "णिश्रिद्रुस्रुभ्यः कर्तरि चङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — RiSridrusruByaH kartari caN"


class Sutra3148:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.48:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.48:root=रामः;pos='),
		('सीता', '', 'प.3.1.48:root=सीता;pos='),
	]

