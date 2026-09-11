# Sutra प.1.1.64: अचोऽन्त्यादि टि
# (Samjna (technical definitions)) — aco'ntyAdi wi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.64"
SUTRA_TEXT = "अचोऽन्त्यादि टि"
SUTRA_DESC = "(Samjna (technical definitions)) — aco'ntyAdi wi"


class Sutra1164:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_64
		return apply_1_1_64(word, pos)

	EXAMPLES = [
		('अच', '', "प.1.1.64:aco'ntyādi-ṭi;input=अच"),
		('अग्नि', '', "प.1.1.64:aco'ntyādi-ṭi;input=अग्नि"),
	]

