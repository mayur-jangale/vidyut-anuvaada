# Sutra प.4.2.92: शेषे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Seze

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.92"
SUTRA_TEXT = "शेषे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Seze"


class Sutra4292:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.92: अग्निः'),
		('रामः', '', 'प.4.2.92: रामः'),
		('सीता', '', 'प.4.2.92: सीता'),
	]

