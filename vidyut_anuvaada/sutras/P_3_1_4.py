# Sutra प.3.1.4: अनुदात्तौ सुप्पितौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anudAttO suppitO

from P_3_1 import apply_3_1_4

SUTRA_CODE = "प.3.1.4"
SUTRA_TEXT = "अनुदात्तौ सुप्पितौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anudAttO suppitO"


class Sutra314:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.4:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.4:root=रामः;pos='),
		('सीता', '', 'प.3.1.4:root=सीता;pos='),
	]

