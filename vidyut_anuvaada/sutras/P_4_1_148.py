# Sutra प.4.1.148: वृद्धाट्ठक् सौवीरेषु बहुलम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAwWak sOvIrezu bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.148"
SUTRA_TEXT = "वृद्धाट्ठक् सौवीरेषु बहुलम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vfdDAwWak sOvIrezu bahulam"


class Sutra41148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

