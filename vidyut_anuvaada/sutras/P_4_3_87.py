# Sutra प.4.3.87: अधिकृत्य कृते ग्रन्थे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aDikftya kfte granTe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.87"
SUTRA_TEXT = "अधिकृत्य कृते ग्रन्थे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aDikftya kfte granTe"


class Sutra4387:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.87: अग्निः'),
		('रामः', '', 'प.4.3.87: रामः'),
		('सीता', '', 'प.4.3.87: सीता'),
	]

