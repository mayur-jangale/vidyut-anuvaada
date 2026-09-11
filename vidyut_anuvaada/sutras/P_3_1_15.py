# Sutra प.3.1.15: कर्मणो रोमन्थतपोभ्यां वर्तिचरोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRo romanTatapoByAM varticaroH

from P_3_1 import apply_3_1_15

SUTRA_CODE = "प.3.1.15"
SUTRA_TEXT = "कर्मणो रोमन्थतपोभ्यां वर्तिचरोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRo romanTatapoByAM varticaroH"


class Sutra3115:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.15:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.15:root=रामः;pos='),
		('सीता', '', 'प.3.1.15:root=सीता;pos='),
	]

