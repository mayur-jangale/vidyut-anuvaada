# Sutra प.4.3.46: ग्रीष्मवसन्तादन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grIzmavasantAdanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.46"
SUTRA_TEXT = "ग्रीष्मवसन्तादन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grIzmavasantAdanyatarasyAm"


class Sutra4346:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.46: अग्निः'),
		('रामः', '', 'प.4.3.46: रामः'),
		('सीता', '', 'प.4.3.46: सीता'),
	]

