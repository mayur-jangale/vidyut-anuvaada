# Sutra प.3.1.47: न दृशः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — na dfSaH

from P_3_1 import apply_3_1_47

SUTRA_CODE = "प.3.1.47"
SUTRA_TEXT = "न दृशः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — na dfSaH"


class Sutra3147:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.47:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.47:root=रामः;pos='),
		('सीता', '', 'प.3.1.47:root=सीता;pos='),
	]

