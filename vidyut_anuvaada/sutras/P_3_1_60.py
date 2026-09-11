# Sutra प.3.1.60: चिण् ते पदः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ciR te padaH

from P_3_1 import apply_3_1_60

SUTRA_CODE = "प.3.1.60"
SUTRA_TEXT = "चिण् ते पदः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ciR te padaH"


class Sutra3160:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.60:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.60:root=रामः;pos='),
		('सीता', '', 'प.3.1.60:root=सीता;pos='),
	]

