# Sutra प.4.3.116: कृते ग्रन्थे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kfte granTe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.116"
SUTRA_TEXT = "कृते ग्रन्थे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kfte granTe"


class Sutra43116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.116: अग्निः'),
		('रामः', '', 'प.4.3.116: रामः'),
		('सीता', '', 'प.4.3.116: सीता'),
	]

