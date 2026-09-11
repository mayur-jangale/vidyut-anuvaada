# Sutra प.3.1.87: कर्मवत् कर्मणा तुल्यक्रियः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmavat karmaRA tulyakriyaH

from P_3_1 import apply_3_1_87

SUTRA_CODE = "प.3.1.87"
SUTRA_TEXT = "कर्मवत् कर्मणा तुल्यक्रियः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmavat karmaRA tulyakriyaH"


class Sutra3187:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_87(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.87:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.87:root=रामः;pos='),
		('सीता', '', 'प.3.1.87:root=सीता;pos='),
	]

