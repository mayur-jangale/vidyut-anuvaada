# Sutra प.3.1.18: सुखादिभ्यः कर्तृवेदनायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — suKAdiByaH kartfvedanAyAm

from P_3_1 import apply_3_1_18

SUTRA_CODE = "प.3.1.18"
SUTRA_TEXT = "सुखादिभ्यः कर्तृवेदनायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — suKAdiByaH kartfvedanAyAm"


class Sutra3118:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.18:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.18:root=रामः;pos='),
		('सीता', '', 'प.3.1.18:root=सीता;pos='),
	]

