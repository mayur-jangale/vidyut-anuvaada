# Sutra प.3.3.71: प्रजने सर्तेः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — prajane sarteH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.71"
SUTRA_TEXT = "प्रजने सर्तेः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — prajane sarteH"


class Sutra3371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

