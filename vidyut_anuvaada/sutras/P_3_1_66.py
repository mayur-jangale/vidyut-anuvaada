# Sutra प.3.1.66: चिण् भावकर्मणोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ciR BAvakarmaRoH

from P_3_1 import apply_3_1_66

SUTRA_CODE = "प.3.1.66"
SUTRA_TEXT = "चिण् भावकर्मणोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ciR BAvakarmaRoH"


class Sutra3166:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.66:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.66:root=रामः;pos='),
		('सीता', '', 'प.3.1.66:root=सीता;pos='),
	]

