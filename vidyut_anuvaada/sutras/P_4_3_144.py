# Sutra प.4.3.144: नित्यं वृद्धशरादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nityaM vfdDaSarAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.144"
SUTRA_TEXT = "नित्यं वृद्धशरादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nityaM vfdDaSarAdiByaH"


class Sutra43144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.144: अग्निः'),
		('रामः', '', 'प.4.3.144: रामः'),
		('सीता', '', 'प.4.3.144: सीता'),
	]

