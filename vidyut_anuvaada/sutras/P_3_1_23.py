# Sutra प.3.1.23: नित्यं कौटिल्ये गतौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM kOwilye gatO

from P_3_1 import apply_3_1_23

SUTRA_CODE = "प.3.1.23"
SUTRA_TEXT = "नित्यं कौटिल्ये गतौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM kOwilye gatO"


class Sutra3123:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_23(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.23:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.23:root=रामः;pos='),
		('सीता', '', 'प.3.1.23:root=सीता;pos='),
	]

