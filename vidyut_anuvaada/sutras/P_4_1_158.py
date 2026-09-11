# Sutra प.4.1.158: वाकिनादीनां कुक् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAkinAdInAM kuk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.158"
SUTRA_TEXT = "वाकिनादीनां कुक् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAkinAdInAM kuk ca"


class Sutra41158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

