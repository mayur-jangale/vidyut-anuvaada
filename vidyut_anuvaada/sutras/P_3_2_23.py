# Sutra प.3.2.23: न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — na SabdaSlokakalahagATAvEracAwusUtramantrapadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.23"
SUTRA_TEXT = "न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — na SabdaSlokakalahagATAvEracAwusUtramantrapadezu"


class Sutra3223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

