# Sutra प.4.2.127: धूमादिभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — DUmAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.127"
SUTRA_TEXT = "धूमादिभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — DUmAdiByaSca"


class Sutra42127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.127: अग्निः'),
		('रामः', '', 'प.4.2.127: रामः'),
		('सीता', '', 'प.4.2.127: सीता'),
	]

