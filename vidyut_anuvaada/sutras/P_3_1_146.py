# Sutra प.3.1.146: गस्थकन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gasTakan

from P_3_1 import apply_3_1_146

SUTRA_CODE = "प.3.1.146"
SUTRA_TEXT = "गस्थकन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gasTakan"


class Sutra31146:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_146(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.146:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.146:root=रामः;pos='),
		('सीता', '', 'प.3.1.146:root=सीता;pos='),
	]

