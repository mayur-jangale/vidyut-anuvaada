# Sutra प.4.4.83: विध्यत्यधनुषा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — viDyatyaDanuzA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.83"
SUTRA_TEXT = "विध्यत्यधनुषा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — viDyatyaDanuzA"


class Sutra4483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.83: अग्निः'),
		('रामः', '', 'प.4.4.83: रामः'),
		('सीता', '', 'प.4.4.83: सीता'),
	]

