# Sutra प.4.1.167: यूनश्च कुत्सायाम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — yUnaSca kutsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.167"
SUTRA_TEXT = "यूनश्च कुत्सायाम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — yUnaSca kutsAyAm"


class Sutra41167:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

