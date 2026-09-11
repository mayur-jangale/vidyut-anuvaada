# Sutra प.4.1.172: कुरुनादिभ्यो ण्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kurunAdiByo RyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.172"
SUTRA_TEXT = "कुरुनादिभ्यो ण्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kurunAdiByo RyaH"


class Sutra41172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

