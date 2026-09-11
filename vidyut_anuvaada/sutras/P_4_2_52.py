# Sutra प.4.2.52: विषयो देशे
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vizayo deSe

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.52"
SUTRA_TEXT = "विषयो देशे"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vizayo deSe"


class Sutra4252:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.52: अग्निः'),
		('रामः', '', 'प.4.2.52: रामः'),
		('सीता', '', 'प.4.2.52: सीता'),
	]

