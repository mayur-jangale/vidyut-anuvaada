# Sutra प.1.2.62: विशाखयोश्च
# (Samjna (technical definitions)) — viSAKayoSca

from P_1_2 import apply_1_2_62

SUTRA_CODE = "प.1.2.62"
SUTRA_TEXT = "विशाखयोश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — viSAKayoSca"


class Sutra1262:
	def apply(self, word, pos):
		return apply_1_2_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-viśākhā:अग्निः'),
		('रामः', '', 'non-viśākhā:रामः'),
		('सीता', '', 'non-viśākhā:सीता'),
	]

