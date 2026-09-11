# Sutra प.4.1.178: न प्राच्यभर्गादियौधेयादिभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — na prAcyaBargAdiyODeyAdiByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.178"
SUTRA_TEXT = "न प्राच्यभर्गादियौधेयादिभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — na prAcyaBargAdiyODeyAdiByaH"


class Sutra41178:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

