# Sutra प.3.1.56: सर्त्तिशास्त्यर्तिभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sarttiSAstyartiByaSca

from P_3_1 import apply_3_1_56

SUTRA_CODE = "प.3.1.56"
SUTRA_TEXT = "सर्त्तिशास्त्यर्तिभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sarttiSAstyartiByaSca"


class Sutra3156:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.56:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.56:root=रामः;pos='),
		('सीता', '', 'प.3.1.56:root=सीता;pos='),
	]

