# Sutra प.3.2.9: हरतेरनुद्यमनेऽच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — harateranudyamane'c

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.9"
SUTRA_TEXT = "हरतेरनुद्यमनेऽच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — harateranudyamane'c"


class Sutra329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

