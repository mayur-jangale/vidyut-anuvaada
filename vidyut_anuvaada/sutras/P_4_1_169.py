# Sutra प.4.1.169: साल्वेयगान्धारिभ्यां च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sAlveyagAnDAriByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.169"
SUTRA_TEXT = "साल्वेयगान्धारिभ्यां च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sAlveyagAnDAriByAM ca"


class Sutra41169:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

