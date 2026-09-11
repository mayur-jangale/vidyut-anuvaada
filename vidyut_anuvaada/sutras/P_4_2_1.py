# Sutra प.4.2.1: तेन रक्तं रागात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tena raktaM rAgAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.1"
SUTRA_TEXT = "तेन रक्तं रागात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tena raktaM rAgAt"


class Sutra421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.1: अग्निः'),
		('रामः', '', 'प.4.2.1: रामः'),
		('सीता', '', 'प.4.2.1: सीता'),
	]

