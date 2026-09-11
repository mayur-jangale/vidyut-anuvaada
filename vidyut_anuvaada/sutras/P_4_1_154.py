# Sutra प.4.1.154: तिकादिभ्यः फिञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tikAdiByaH PiY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.154"
SUTRA_TEXT = "तिकादिभ्यः फिञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tikAdiByaH PiY"


class Sutra41154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

