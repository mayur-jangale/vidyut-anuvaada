# Sutra प.4.4.15: हरत्युत्सङ्गादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — haratyutsaNgAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.15"
SUTRA_TEXT = "हरत्युत्सङ्गादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — haratyutsaNgAdiByaH"


class Sutra4415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.15: अग्निः'),
		('रामः', '', 'प.4.4.15: रामः'),
		('सीता', '', 'प.4.4.15: सीता'),
	]

