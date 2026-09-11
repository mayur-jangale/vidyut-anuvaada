# Sutra प.4.3.79: पितुर्यच्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — pituryacca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.79"
SUTRA_TEXT = "पितुर्यच्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — pituryacca"


class Sutra4379:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.79: अग्निः'),
		('रामः', '', 'प.4.3.79: रामः'),
		('सीता', '', 'प.4.3.79: सीता'),
	]

