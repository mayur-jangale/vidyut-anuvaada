# Sutra प.4.1.170: द्व्यञ्मगधकलिङ्गसूरमसादण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvyaYmagaDakaliNgasUramasAdaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.170"
SUTRA_TEXT = "द्व्यञ्मगधकलिङ्गसूरमसादण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvyaYmagaDakaliNgasUramasAdaR"


class Sutra41170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

