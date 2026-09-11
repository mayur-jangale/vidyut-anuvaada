# Sutra प.1.1.47: मिदचोऽन्त्यात्परः
# (Samjna (technical definitions)) — midaco'ntyAtparaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.47"
SUTRA_TEXT = "मिदचोऽन्त्यात्परः"
SUTRA_DESC = "(Samjna (technical definitions)) — midaco'ntyAtparaH"


class Sutra1147:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_47
		return apply_1_1_47(word, pos)

	EXAMPLES = [
		('परः', '', "प.1.1.47:midaco'ntyātparaḥ;input=परः"),
		('अग्नि', '', "प.1.1.47:midaco'ntyātparaḥ;input=अग्नि"),
	]

