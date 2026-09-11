# Sutra प.3.2.42: सर्वकूलाभ्रकरीषेषु कषः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sarvakUlABrakarIzezu kazaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.42"
SUTRA_TEXT = "सर्वकूलाभ्रकरीषेषु कषः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sarvakUlABrakarIzezu kazaH"


class Sutra3242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

