# Sutra प.3.1.14: कष्टाय क्रमणे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kazwAya kramaRe

from P_3_1 import apply_3_1_14

SUTRA_CODE = "प.3.1.14"
SUTRA_TEXT = "कष्टाय क्रमणे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kazwAya kramaRe"


class Sutra3114:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.14:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.14:root=रामः;pos='),
		('सीता', '', 'प.3.1.14:root=सीता;pos='),
	]

