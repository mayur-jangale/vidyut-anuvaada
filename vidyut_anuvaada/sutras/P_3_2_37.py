# Sutra प.3.2.37: उग्रम्पश्येरम्मदपाणिन्धमाश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — ugrampaSyerammadapARinDamASca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.37"
SUTRA_TEXT = "उग्रम्पश्येरम्मदपाणिन्धमाश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — ugrampaSyerammadapARinDamASca"


class Sutra3237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

