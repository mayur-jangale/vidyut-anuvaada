# Sutra प.3.3.64: नौ गदनदपठस्वनः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO gadanadapaWasvanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.64"
SUTRA_TEXT = "नौ गदनदपठस्वनः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nO gadanadapaWasvanaH"


class Sutra3364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

