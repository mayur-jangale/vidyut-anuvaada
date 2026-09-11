# Sutra प.4.4.81: हलसीराट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — halasIrAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.81"
SUTRA_TEXT = "हलसीराट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — halasIrAwWak"


class Sutra4481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.81: अग्निः'),
		('रामः', '', 'प.4.4.81: रामः'),
		('सीता', '', 'प.4.4.81: सीता'),
	]

