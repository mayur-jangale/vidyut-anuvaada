# Sutra प.3.1.71: यसोऽनुपसर्गात्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaso'nupasargAt

from P_3_1 import apply_3_1_71

SUTRA_CODE = "प.3.1.71"
SUTRA_TEXT = "यसोऽनुपसर्गात्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yaso'nupasargAt"


class Sutra3171:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.71:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.71:root=रामः;pos='),
		('सीता', '', 'प.3.1.71:root=सीता;pos='),
	]

