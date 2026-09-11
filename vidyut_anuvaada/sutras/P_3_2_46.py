# Sutra प.3.2.46: संज्ञायां भृतॄवृजिधारिसहितपिदमः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMjYAyAM BftFvfjiDArisahitapidamaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.46"
SUTRA_TEXT = "संज्ञायां भृतॄवृजिधारिसहितपिदमः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saMjYAyAM BftFvfjiDArisahitapidamaH"


class Sutra3246:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

