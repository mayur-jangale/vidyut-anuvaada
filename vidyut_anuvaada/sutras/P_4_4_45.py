# Sutra प.4.4.45: सेनाया वा
# (Sup-sthāna (nominal endings) and kṛt-affixes) — senAyA vA

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.45"
SUTRA_TEXT = "सेनाया वा"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — senAyA vA"


class Sutra4445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.45: अग्निः'),
		('रामः', '', 'प.4.4.45: रामः'),
		('सीता', '', 'प.4.4.45: सीता'),
	]

