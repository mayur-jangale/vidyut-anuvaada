# Sutra प.3.1.83: हलः श्नः शानज्झौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — halaH SnaH SAnajJO

from P_3_1 import apply_3_1_83

SUTRA_CODE = "प.3.1.83"
SUTRA_TEXT = "हलः श्नः शानज्झौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — halaH SnaH SAnajJO"


class Sutra3183:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_83(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.83:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.83:root=रामः;pos='),
		('सीता', '', 'प.3.1.83:root=सीता;pos='),
	]

