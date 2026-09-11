# Sutra प.3.3.19: अकर्तरि च कारके संज्ञायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — akartari ca kArake saMjYAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.19"
SUTRA_TEXT = "अकर्तरि च कारके संज्ञायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — akartari ca kArake saMjYAyAm"


class Sutra3319:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

