# Sutra प.3.3.82: करणेऽयोविद्रुषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRe'yovidruzu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.82"
SUTRA_TEXT = "करणेऽयोविद्रुषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karaRe'yovidruzu"


class Sutra3382:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

