# Sutra प.4.4.52: लवणाट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — lavaRAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.52"
SUTRA_TEXT = "लवणाट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — lavaRAwWaY"


class Sutra4452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.52: अग्निः'),
		('रामः', '', 'प.4.4.52: रामः'),
		('सीता', '', 'प.4.4.52: सीता'),
	]

