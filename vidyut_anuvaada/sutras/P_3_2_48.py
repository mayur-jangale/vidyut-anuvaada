# Sutra प.3.2.48: अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — antAtyantADvadUrapArasarvAnantezu qaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.48"
SUTRA_TEXT = "अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — antAtyantADvadUrapArasarvAnantezu qaH"


class Sutra3248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

