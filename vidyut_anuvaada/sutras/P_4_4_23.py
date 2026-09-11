# Sutra प.4.4.23: चूर्णादिनिः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — cUrRAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.23"
SUTRA_TEXT = "चूर्णादिनिः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — cUrRAdiniH"


class Sutra4423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.23: अग्निः'),
		('रामः', '', 'प.4.4.23: रामः'),
		('सीता', '', 'प.4.4.23: सीता'),
	]

