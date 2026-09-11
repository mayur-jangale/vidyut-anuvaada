# Sutra प.3.1.49: विभाषा धेट्श्व्योः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA DewSvyoH

from P_3_1 import apply_3_1_49

SUTRA_CODE = "प.3.1.49"
SUTRA_TEXT = "विभाषा धेट्श्व्योः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA DewSvyoH"


class Sutra3149:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.49:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.49:root=रामः;pos='),
		('सीता', '', 'प.3.1.49:root=सीता;pos='),
	]

