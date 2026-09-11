# Sutra प.4.4.82: संज्ञायां जन्याः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM janyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.82"
SUTRA_TEXT = "संज्ञायां जन्याः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM janyAH"


class Sutra4482:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.82: अग्निः'),
		('रामः', '', 'प.4.4.82: रामः'),
		('सीता', '', 'प.4.4.82: सीता'),
	]

