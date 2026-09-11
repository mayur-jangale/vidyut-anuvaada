# Sutra प.3.2.35: विध्वरुषोस्तुदः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viDvaruzostudaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.35"
SUTRA_TEXT = "विध्वरुषोस्तुदः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viDvaruzostudaH"


class Sutra3235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

