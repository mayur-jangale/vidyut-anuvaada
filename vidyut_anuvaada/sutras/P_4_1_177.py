# Sutra प.4.1.177: अतश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ataSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.177"
SUTRA_TEXT = "अतश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ataSca"


class Sutra41177:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

