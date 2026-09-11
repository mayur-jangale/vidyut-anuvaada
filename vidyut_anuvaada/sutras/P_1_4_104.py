# Sutra प.1.4.104: विभक्तिश्च
# (Samjna (technical definitions)) — viBaktiSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.104"
SUTRA_TEXT = "विभक्तिश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — viBaktiSca"


class Sutra14104:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_104
		return apply_1_4_104(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-vibhakti:अग्निः'),
		('रामः', '', 'no-vibhakti:रामः'),
		('सीता', '', 'no-vibhakti:सीता'),
	]

