# Sutra प.1.2.17: स्था घ्वोरिच्च
# (Samjna (technical definitions)) — sTA Gvoricca

from P_1_2 import apply_1_2_17

SUTRA_CODE = "प.1.2.17"
SUTRA_TEXT = "स्था घ्वोरिच्च"
SUTRA_DESC = "(Samjna (technical definitions)) — sTA Gvoricca"


class Sutra1217:
	def apply(self, word, pos):
		return apply_1_2_17(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-sthā-ghū:अग्निः'),
		('रामः', '', 'non-sthā-ghū:रामः'),
		('सीता', '', 'non-sthā-ghū:सीता'),
	]

