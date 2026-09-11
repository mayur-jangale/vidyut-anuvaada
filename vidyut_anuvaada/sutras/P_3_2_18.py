# Sutra प.3.2.18: पुरोऽग्रतोऽग्रेषु सर्तेः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — puro'grato'grezu sarteH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.18"
SUTRA_TEXT = "पुरोऽग्रतोऽग्रेषु सर्तेः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — puro'grato'grezu sarteH"


class Sutra3218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

