# Sutra प.3.1.51: नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nonayatiDvanayatyelayatyardayatiByaH

from P_3_1 import apply_3_1_51

SUTRA_CODE = "प.3.1.51"
SUTRA_TEXT = "नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nonayatiDvanayatyelayatyardayatiByaH"


class Sutra3151:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.51:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.51:root=रामः;pos='),
		('सीता', '', 'प.3.1.51:root=सीता;pos='),
	]

