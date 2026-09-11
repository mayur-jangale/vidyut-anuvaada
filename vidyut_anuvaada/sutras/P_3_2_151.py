# Sutra प.3.2.151: क्रुधमण्डार्थेभ्यश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kruDamaRqArTeByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.151"
SUTRA_TEXT = "क्रुधमण्डार्थेभ्यश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kruDamaRqArTeByaSca"


class Sutra32151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

