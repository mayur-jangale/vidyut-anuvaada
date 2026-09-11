# Sutra प.4.4.50: अवक्रयः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — avakrayaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.50"
SUTRA_TEXT = "अवक्रयः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — avakrayaH"


class Sutra4450:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.50: अग्निः'),
		('रामः', '', 'प.4.4.50: रामः'),
		('सीता', '', 'प.4.4.50: सीता'),
	]

