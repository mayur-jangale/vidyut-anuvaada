# Sutra प.4.2.133: कच्छादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kacCAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.133"
SUTRA_TEXT = "कच्छादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kacCAdiByaSca"


class Sutra42133:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.133: अग्निः'),
		('रामः', '', 'प.4.2.133: रामः'),
		('सीता', '', 'प.4.2.133: सीता'),
	]

