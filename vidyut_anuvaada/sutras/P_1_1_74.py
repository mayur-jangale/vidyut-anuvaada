# Sutra प.1.1.74: त्यदादीनि च
# (Samjna (technical definitions)) — tyadAdIni ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.74"
SUTRA_TEXT = "त्यदादीनि च"
SUTRA_DESC = "(Samjna (technical definitions)) — tyadAdIni ca"


class Sutra1174:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_74
		return apply_1_1_74(word, pos)

	EXAMPLES = [
		('तत्', '', 'tyad-sarvanama:तत्'),
		('यत्', '', 'tyad-sarvanama:यत्'),
		('देव', '', 'non-tyad:देव'),
	]

