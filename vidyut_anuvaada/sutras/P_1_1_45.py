# Sutra प.1.1.45: इग्यणः सम्प्रसारणम्
# (Samjna (technical definitions)) — igyaRaH samprasAraRam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.45"
SUTRA_TEXT = "इग्यणः सम्प्रसारणम्"
SUTRA_DESC = "(Samjna (technical definitions)) — igyaRaH samprasAraRam"


class Sutra1145:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_45
		return apply_1_1_45(word, pos)

	EXAMPLES = [
		('इच्', '', 'प.1.1.45:igyaṇaḥ-samprasāraṇam;input=इच्'),
		('अग्नि', '', 'प.1.1.45:igyaṇaḥ-samprasāraṇam;input=अग्नि'),
	]

