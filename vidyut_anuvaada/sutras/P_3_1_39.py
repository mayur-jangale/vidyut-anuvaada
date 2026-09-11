# Sutra प.3.1.39: भीह्रीभृहुवां श्लुवच्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BIhrIBfhuvAM Sluvacca

from P_3_1 import apply_3_1_39

SUTRA_CODE = "प.3.1.39"
SUTRA_TEXT = "भीह्रीभृहुवां श्लुवच्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BIhrIBfhuvAM Sluvacca"


class Sutra3139:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.39:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.39:root=रामः;pos='),
		('सीता', '', 'प.3.1.39:root=सीता;pos='),
	]

