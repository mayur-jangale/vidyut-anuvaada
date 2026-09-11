# Sutra प.3.1.45: शल इगुपधादनिटः क्सः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sala igupaDAdaniwaH ksaH

from P_3_1 import apply_3_1_45

SUTRA_CODE = "प.3.1.45"
SUTRA_TEXT = "शल इगुपधादनिटः क्सः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Sala igupaDAdaniwaH ksaH"


class Sutra3145:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.45:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.45:root=रामः;pos='),
		('सीता', '', 'प.3.1.45:root=सीता;pos='),
	]

