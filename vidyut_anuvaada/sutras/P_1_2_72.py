# Sutra प.1.2.72: त्यदादीनि सर्वैर्नित्यम्
# (Samjna (technical definitions)) — tyadAdIni sarvErnityam

from P_1_2 import apply_1_2_72

SUTRA_CODE = "प.1.2.72"
SUTRA_TEXT = "त्यदादीनि सर्वैर्नित्यम्"
SUTRA_DESC = "(Samjna (technical definitions)) — tyadAdIni sarvErnityam"


class Sutra1272:
	def apply(self, word, pos):
		return apply_1_2_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-tyad:अग्निः'),
		('रामः', '', 'non-tyad:रामः'),
		('सीता', '', 'non-tyad:सीता'),
	]

