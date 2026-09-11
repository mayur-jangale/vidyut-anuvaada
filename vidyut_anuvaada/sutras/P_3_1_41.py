# Sutra प.3.1.41: विदाङ्कुर्वन्त्वित्यन्यतरस्याम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vidANkurvantvityanyatarasyAm

from P_3_1 import apply_3_1_41

SUTRA_CODE = "प.3.1.41"
SUTRA_TEXT = "विदाङ्कुर्वन्त्वित्यन्यतरस्याम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vidANkurvantvityanyatarasyAm"


class Sutra3141:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.41:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.41:root=रामः;pos='),
		('सीता', '', 'प.3.1.41:root=सीता;pos='),
	]

