# Sutra प.1.1.53: ङिच्च
# (Samjna (technical definitions)) — Nicca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.53"
SUTRA_TEXT = "ङिच्च"
SUTRA_DESC = "(Samjna (technical definitions)) — Nicca"


class Sutra1153:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_53
		return apply_1_1_53(word, pos)

	EXAMPLES = [
		('ङिच्', '', 'प.1.1.53:ṅicca;input=ङिच्'),
		('अग्नि', '', 'प.1.1.53:ṅicca;input=अग्नि'),
	]

