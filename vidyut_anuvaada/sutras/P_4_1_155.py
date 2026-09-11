# Sutra प.4.1.155: कौसल्यकार्मार्याभ्यां च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kOsalyakArmAryAByAM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.155"
SUTRA_TEXT = "कौसल्यकार्मार्याभ्यां च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kOsalyakArmAryAByAM ca"


class Sutra41155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

