# Sutra प.4.4.84: धनगणं लब्धा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — DanagaRaM labDA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.84"
SUTRA_TEXT = "धनगणं लब्धा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — DanagaRaM labDA"


class Sutra4484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.84: अग्निः'),
		('रामः', '', 'प.4.4.84: रामः'),
		('सीता', '', 'प.4.4.84: सीता'),
	]

