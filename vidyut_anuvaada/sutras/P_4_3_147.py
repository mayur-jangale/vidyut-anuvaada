# Sutra प.4.3.147: संज्ञायां कन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM kan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.147"
SUTRA_TEXT = "संज्ञायां कन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM kan"


class Sutra43147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.147: अग्निः'),
		('रामः', '', 'प.4.3.147: रामः'),
		('सीता', '', 'प.4.3.147: सीता'),
	]

