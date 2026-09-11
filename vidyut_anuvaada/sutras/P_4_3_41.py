# Sutra प.4.3.41: संभूते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMBUte

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.41"
SUTRA_TEXT = "संभूते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMBUte"


class Sutra4341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.41: अग्निः'),
		('रामः', '', 'प.4.3.41: रामः'),
		('सीता', '', 'प.4.3.41: सीता'),
	]

