# Sutra प.4.2.51: इनित्रकट्यचश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — initrakawyacaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.51"
SUTRA_TEXT = "इनित्रकट्यचश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — initrakawyacaSca"


class Sutra4251:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.51: अग्निः'),
		('रामः', '', 'प.4.2.51: रामः'),
		('सीता', '', 'प.4.2.51: सीता'),
	]

